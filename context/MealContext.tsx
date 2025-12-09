import React, { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { MealPlan, AppSettings, Recipe, PlannedMeal, MealContextType, InventoryItem, IngredientSuggestion, BackendUserData } from '../types';
import { translations, TranslationKey } from '../translations';
import { fetchRecipes, createRecipe as apiCreateRecipe, fetchIngredients, createIngredient as apiCreateIngredient, fetchUserData, saveUserData } from '../services/api';

const MealContext = createContext<MealContextType | undefined>(undefined);

// Helper to format Date to YYYY-MM-DD local time
const formatDate = (date: Date): string => {
  const offset = date.getTimezoneOffset();
  const localDate = new Date(date.getTime() - (offset * 60 * 1000));
  return localDate.toISOString().split('T')[0];
};

export const MealProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  // --- Data State ---
  const [recipes, setRecipes] = useState<Recipe[]>([]);
  const [availableIngredients, setAvailableIngredients] = useState<IngredientSuggestion[]>([]);
  
  // User Data State - Initialize with defaults, will be populated by API
  const [settings, setSettings] = useState<AppSettings>({
    startDate: formatDate(new Date()),
    daysDuration: 5,
    language: 'sk'
  });
  const [plan, setPlan] = useState<MealPlan>({});
  const [inventory, setInventory] = useState<InventoryItem[]>([]);
  
  const [isLoading, setIsLoading] = useState(true);
  const [isTestMode, setIsTestMode] = useState(false);
  const [isInitialized, setIsInitialized] = useState(false); // Flag to prevent saving empty state on load
  const [saveError, setSaveError] = useState(false);

  // Load Data on Mount
  useEffect(() => {
    const loadData = async () => {
      setIsLoading(true);
      
      // 1. Recipes (Needed first to hydrate plan)
      const { data: recipeData, isTestMode: testMode } = await fetchRecipes();
      setRecipes(recipeData);
      setIsTestMode(testMode);
      
      // 2. Ingredients
      const ingredientsData = await fetchIngredients();
      setAvailableIngredients(ingredientsData);

      // 3. User Data (Settings, Plan, Inventory)
      // We fetch all data without filters to have full client state
      const userData = await fetchUserData();
      
      if (userData) {
          // Sync Settings
          if (userData.settings) {
              setSettings(userData.settings);
          }
          
          // Sync Inventory
          if (userData.inventory) {
              setInventory(userData.inventory);
          }
          
          // Sync Plan - Needs rehydration (joining with Recipes)
          if (userData.plan) {
             const restoredPlan: MealPlan = {};
             userData.plan.forEach(item => {
                 const recipe = recipeData.find(r => r.id === item.recipeId);
                 if (recipe) {
                     if (!restoredPlan[item.date]) restoredPlan[item.date] = [];
                     restoredPlan[item.date].push({
                         ...recipe,
                         uid: item.uid,
                         portions: item.portions
                     });
                 }
             });
             setPlan(restoredPlan);
          }
      }
      
      setIsLoading(false);
      setIsInitialized(true);
    };
    loadData();
  }, []);

  // --- Persistence (Autosave) ---
  useEffect(() => {
    // Don't save if we haven't loaded data yet, or if we are in test mode (optional, but robust)
    if (!isInitialized) return;

    const timeoutId = setTimeout(async () => {
        // Flatten Plan for Backend
        const planPayload: any[] = [];
        Object.entries(plan).forEach(([date, meals]) => {
            meals.forEach(meal => {
                planPayload.push({
                    uid: meal.uid,
                    date: date,
                    recipeId: meal.id,
                    portions: meal.portions
                });
            });
        });

        // Backend expects InventoryItem array which matches our state structure
        // Backend expects Settings which matches our state structure

        const payload: BackendUserData = {
            settings,
            inventory,
            plan: planPayload
        };

        const success = await saveUserData(payload);
        setSaveError(!success);

    }, 1000); // 1s Debounce

    return () => clearTimeout(timeoutId);
  }, [plan, inventory, settings, isInitialized]);

  const updateSettings = (newSettings: Partial<AppSettings>) => {
    setSettings(prev => ({ ...prev, ...newSettings }));
  };

  const addMealToDay = (date: string, recipe: Recipe, portions?: number) => {
    setPlan(prev => {
      const currentDayMeals = prev[date] || [];
      const newMeal: PlannedMeal = {
        ...recipe,
        portions: portions !== undefined ? portions : (recipe.defaultPortions || 1),
        uid: Date.now().toString() + Math.random().toString(36).substr(2, 9)
      };
      return {
        ...prev,
        [date]: [...currentDayMeals, newMeal]
      };
    });
  };

  const removeMealFromDay = (date: string, uid: string) => {
    setPlan(prev => {
      const currentDayMeals = prev[date] || [];
      const updatedMeals = currentDayMeals.filter(m => m.uid !== uid);
      return {
        ...prev,
        [date]: updatedMeals
      };
    });
  };

  const updateMealPortions = (date: string, uid: string, change: number) => {
     setPlan(prev => {
        const currentDayMeals = prev[date] || [];
        const updatedMeals = currentDayMeals.map(meal => {
           if (meal.uid === uid) {
             const newPortions = Math.max(1, meal.portions + change);
             return { ...meal, portions: newPortions };
           }
           return meal;
        });
        return {
           ...prev,
           [date]: updatedMeals
        };
     });
  };

  const toggleInventory = (recipeId: number) => {
    setInventory(prev => {
      const exists = prev.find(item => item.recipeId === recipeId);
      if (exists) {
        return prev.filter(item => item.recipeId !== recipeId);
      } else {
        const recipe = recipes.find(r => r.id === recipeId);
        return [...prev, {
          recipeId,
          portions: recipe?.defaultPortions || 1,
          uid: Date.now().toString() + Math.random().toString(36).substr(2, 9)
        }];
      }
    });
  };
  
  const removeFromInventory = (uid: string) => {
    setInventory(prev => prev.filter(item => item.uid !== uid));
  };

  const updateInventoryPortions = (uid: string, change: number) => {
    setInventory(prev => prev.map(item => {
      if (item.uid === uid) {
        return { ...item, portions: Math.max(1, item.portions + change) };
      }
      return item;
    }));
  };

  const consumeInventoryPortions = (uid: string, amount: number) => {
    setInventory(prev => {
      return prev.map(item => {
        if (item.uid === uid) {
          const remaining = item.portions - amount;
          return { ...item, portions: remaining };
        }
        return item;
      }).filter(item => item.portions > 0.01);
    });
  };

  const createRecipe = async (data: any) => {
    // 1. Create on Backend (or fallback)
    const newRecipe = await apiCreateRecipe(data, availableIngredients);
    
    // 2. Reload all recipes to ensure sync with backend ID generation and calculations
    const { data: allRecipes, isTestMode: testMode } = await fetchRecipes();
    
    // If backend is down (testMode), fetchRecipes returns fallback data which 
    // DOES NOT contain our newly created mock recipe. We must manually append it.
    if (testMode) {
       setRecipes(prev => [...prev, newRecipe]);
       setIsTestMode(true);
    } else {
       setRecipes(allRecipes);
    }
    
    return newRecipe;
  };

  const addIngredient = async (ingredient: Omit<IngredientSuggestion, 'id'>) => {
    const newIngredient = await apiCreateIngredient(ingredient);
    setAvailableIngredients(prev => [...prev, newIngredient]);
    return newIngredient;
  };

  const t = (key: TranslationKey): string => {
    return translations[settings.language][key] || key;
  };

  return (
    <MealContext.Provider value={{
      recipes,
      plan,
      inventory,
      settings,
      availableIngredients,
      updateSettings,
      addMealToDay,
      removeMealFromDay,
      updateMealPortions,
      toggleInventory,
      updateInventoryPortions,
      consumeInventoryPortions,
      removeFromInventory,
      createRecipe,
      addIngredient,
      t,
      language: settings.language,
      isTestMode,
      saveError
    }}>
      {children}
    </MealContext.Provider>
  );
};

export const useMealContext = () => {
  const context = useContext(MealContext);
  if (!context) {
    throw new Error("useMealContext must be used within a MealProvider");
  }
  return context;
};