import React, { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import {
  Recipe,
  MealPlan,
  Ingredient,
  AppSettings,
  UserInventoryItem,
  IngredientSuggestion
} from '../types';
import {
  fetchUserData,
  saveUserData,
  createRecipe as apiCreateRecipe,
  createIngredient as apiCreateIngredient,
  fetchIngredients,
  fetchRecipes,
  adaptBackendRecipe
} from '../services/api';
import { transformBackendPlanToMealPlan, transformMealPlanToBackendPlan } from '../services/transformers';
import { translations, TranslationKey } from '../translations';
import { FALLBACK_DATA } from '../services/fallbackData';

interface MealContextType {
  recipes: Recipe[];
  plan: MealPlan;
  inventory: UserInventoryItem[];
  settings: AppSettings;
  availableIngredients: IngredientSuggestion[];
  updateSettings: (newSettings: Partial<AppSettings>) => void;
  addMealToDay: (date: string, recipeId: number) => void;
  removeMealFromDay: (date: string, uid: string) => void;
  updateMealPortions: (date: string, uid: string, change: number) => void;
  toggleInventory: (date: string, uid: string) => void;
  updateInventoryPortions: (uid: string, amount: number) => void;
  consumeInventoryPortions: (uid: string, amount: number) => void;
  removeFromInventory: (uid: string) => void;
  createRecipe: (data: any) => Promise<Recipe>;
  addIngredient: (ingredient: Omit<IngredientSuggestion, 'id'>) => Promise<IngredientSuggestion>;
  t: (key: TranslationKey) => string;
  language: 'sk' | 'en';
  isTestMode: boolean;
  saveError: string | null;
}

const MealContext = createContext<MealContextType | undefined>(undefined);

const validateSettings = (settings: Partial<AppSettings> | undefined) => {
  if (!settings || !settings.language || !settings.startDate || settings.daysDuration === undefined) {
    throw new Error("Settings not loaded correctly");
  }
};

export const MealProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [recipes, setRecipes] = useState<Recipe[]>([]);
  const [plan, setPlan] = useState<MealPlan>({});
  const [inventory, setInventory] = useState<UserInventoryItem[]>([]);
  const [settings, setSettings] = useState<AppSettings>({
    language: 'sk',
    startDate: new Date().toISOString().split('T')[0],
    daysDuration: 7
  });
  const [availableIngredients, setAvailableIngredients] = useState<IngredientSuggestion[]>([]);
  const [isTestMode, setIsTestMode] = useState(false);
  const [saveError, setSaveError] = useState<string | null>(null);
  const [isInitialized, setIsInitialized] = useState(false);

  // Load initial data
  useEffect(() => {
    const loadData = async () => {
      try {
        const [userData, allRecipes, allIngredients] = await Promise.all([
          fetchUserData(),
          fetchRecipes(),
          fetchIngredients()
        ]);

        if (userData) {
          // Flatten array -> Record<string, PlannedMeal[]>
          const parsedPlan = transformBackendPlanToMealPlan(userData.plan, allRecipes.data);
          setPlan(parsedPlan);

          setInventory(userData.inventory || []);
          validateSettings(userData.settings);
          setSettings(userData.settings);
        }
        setRecipes(allRecipes.data || []);
        setAvailableIngredients(allIngredients);
        // If recipes indicates test mode, we can trust that
        if (allRecipes.isTestMode) setIsTestMode(true);
        setIsInitialized(true);
      } catch (error) {
        console.error("Failed to load data", error);
        // Use fallback if critical failure
        setRecipes(FALLBACK_DATA.map(adaptBackendRecipe));
        setIsTestMode(true);
        setIsInitialized(true);
      }
    };
    loadData();
  }, []);

  // Save changes
  const save = async (newPlan: MealPlan, newInventory: UserInventoryItem[], newSettings: AppSettings) => {
    // Optimistic update
    try {
      // Flatten plan for API
      // Convert MealPlan to BackendPlanItem[]
      const planItems = transformMealPlanToBackendPlan(newPlan);

      const success = await saveUserData({
        settings: newSettings,
        plan: planItems,
        inventory: newInventory
      });

      if (!success) {
        setSaveError("Failed to save changes to server.");
        // In a real app we might revert state here
      } else {
        setSaveError(null);
      }
    } catch (e) {
      setSaveError("Network error saving changes.");
    }
  };

  const updateSettings = (newSettings: Partial<AppSettings>) => {
    const updated = { ...settings, ...newSettings };
    setSettings(updated);
    save(plan, inventory, updated);
  };

  const addMealToDay = (date: string, recipeOrRecipeId: Recipe | number, portions?: number) => {
    let recipe: Recipe | undefined;

    if (typeof recipeOrRecipeId === 'number') {
      recipe = recipes.find(r => r.id === recipeOrRecipeId);
    } else {
      recipe = recipeOrRecipeId;
    }

    if (!recipe) return;

    const newMeal = {
      uid: Math.random().toString(36).substr(2, 9),
      recipeId: recipe.id,
      title: recipe.title, // Add title and other props to match PlannedMeal if needed, though state stores full object usually or just ID?
      // Wait, MealPlan stores PlannedMeal which extends Recipe.
      // We need to store the FULL recipe data or at least what's needed for display if we don't look it up every time.
      // But looking at lines 103-110 in save(), we just save what's in plan. 
      // Lines 77 setPlan(userData.plan).
      // Logic suggests we store full meal objects.
      ...recipe,
      portions: portions || recipe.defaultPortions || 1,
      isCooked: false
    };

    setPlan(prev => {
      const currentMeals = prev[date] || [];
      const next = { ...prev, [date]: [...currentMeals, newMeal] };
      save(next, inventory, settings);
      return next;
    });
  };



  const removeMealFromDay = (date: string, uid: string) => {
    setPlan(prev => {
      const current = prev[date] || [];
      const next = { ...prev, [date]: current.filter(m => m.uid !== uid) };
      save(next, inventory, settings);
      return next;
    });
  };

  const updateMealPortions = (date: string, uid: string, change: number) => {
    setPlan(prev => {
      const current = prev[date] || [];
      const updated = current.map(m => {
        if (m.uid === uid) {
          return { ...m, portions: Math.max(0.1, m.portions + change) };
        }
        return m;
      });
      const next = { ...prev, [date]: updated };
      save(next, inventory, settings);
      return next;
    });
  };

  const toggleInventory = (recipeId: number) => {
    setInventory(prev => {
      const exists = prev.find(item => item.recipeId === recipeId);
      let next;
      if (exists) {
        // Remove
        next = prev.filter(item => item.recipeId !== recipeId);
      } else {
        // Add
        const newInv: UserInventoryItem = {
          uid: Math.random().toString(36).substr(2, 9),
          recipeId: recipeId,
          portions: 1 // Default portions
        };
        next = [...prev, newInv];
      }
      save(plan, next, settings);
      return next;
    });
  };

  const updateInventoryPortions = (uid: string, amount: number) => {
    setInventory(prev => {
      const next = prev.map(item => item.uid === uid ? { ...item, portions: amount } : item);
      save(plan, next, settings);
      return next;
    });
  };

  const consumeInventoryPortions = (uid: string, amount: number) => {
    setInventory(prev => {
      const next = prev.map(item => item.uid === uid ? { ...item, portions: Math.max(0, item.portions - amount) } : item)
        .filter(item => item.portions > 0.01);
      save(plan, next, settings);
      return next;
    });
  };

  const removeFromInventory = (uid: string) => {
    setInventory(prev => {
      const next = prev.filter(item => item.uid !== uid);
      save(plan, next, settings);
      return next;
    });
  };

  const createRecipe = async (data: any) => {
    // data likely matches API payload
    const newRecipe = await apiCreateRecipe(data, availableIngredients); // simplistic
    setRecipes(prev => [...prev, newRecipe]);
    return newRecipe;
  };

  const addIngredient = async (ing: Omit<IngredientSuggestion, 'id'>) => {
    const newIng = await apiCreateIngredient(ing);
    setAvailableIngredients(prev => [...prev, newIng]);
    return newIng;
  };

  const t = (key: TranslationKey): string => {
    const lang = settings.language && translations[settings.language] ? settings.language : 'sk';
    return translations[lang][key] || key;
  };

  if (!isInitialized) {
    return (
      <div className="fixed inset-0 flex items-center justify-center bg-gray-50">
        <div className="flex flex-col items-center gap-4">
          <div className="h-12 w-12 animate-spin rounded-full border-4 border-primary border-t-transparent"></div>
          <p className="text-gray-500 font-medium animate-pulse">Načítavam dáta...</p>
        </div>
      </div>
    );
  }

  return (
    <MealContext.Provider value={{
      recipes, plan, inventory, settings, availableIngredients,
      updateSettings, addMealToDay, removeMealFromDay, updateMealPortions,
      toggleInventory, updateInventoryPortions, consumeInventoryPortions,
      removeFromInventory, createRecipe, addIngredient,
      t, language: settings.language, isTestMode, saveError
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
