import { Recipe, IngredientSuggestion, BackendUserData } from '../types';
import { FALLBACK_DATA } from './fallbackData';
import { MOCK_INGREDIENTS } from './mockIngredients';

// Configuration: API Base URL
// 1. Tries to use environment variable (standard for Create React App / Vite)
// 2. Fallbacks to localhost for local development
const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

// 1. Define the exact shape of your Backend Data
export interface BackendRecipe {
  id: number;
  name: string;
  defaultPortions: number;
  ingredients: Array<{
    ingredientId: string; // ID reference to IngredientSuggestion
    name: string;         // Snapshot of name for display
    quantity: number;
    unit: string;
  }>;
  instructions: string;
  nutrition: {
    energy: number;       // kcal
    protein: number;
    carbs: number;        // maps to carbs
    fat: number;
    fiber?: number;
    sugar?: number;
  };
  tags: string[];
}

export interface BackendIngredient {
  id: number;
  name: string;
  energy: number;
  protein: number;
  carbs: number;
  fat: number;
  fiber?: number;
  sugar?: number;
}

// Placeholder images to make the UI look good without real photos
const PLACEHOLDER_IMAGES = [
  "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80",
  "https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?auto=format&fit=crop&w=800&q=80",
  "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?auto=format&fit=crop&w=800&q=80",
  "https://images.unsplash.com/photo-1482049016688-2d3e1b311543?auto=format&fit=crop&w=800&q=80",
  "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=800&q=80",
  "https://images.unsplash.com/photo-1473093295043-cdd812d0e601?auto=format&fit=crop&w=800&q=80",
  "https://images.unsplash.com/photo-1490645935967-10de6ba17061?auto=format&fit=crop&w=800&q=80",
  "https://images.unsplash.com/photo-1498837167922-ddd27525d352?auto=format&fit=crop&w=800&q=80"
];

const getImageForId = (id: number) => {
  return PLACEHOLDER_IMAGES[id % PLACEHOLDER_IMAGES.length];
};

// 2. The Adapter Functions: Transforms Backend -> Frontend
export const adaptBackendRecipe = (data: BackendRecipe): Recipe => {
  // Format ingredients using the snapshot name from the backend object
  const formattedIngredients = data.ingredients.map(ing => 
    `${ing.quantity}${ing.unit} ${ing.name}`
  );

  // Split text block instructions into steps
  let steps = data.instructions
    .split('. ')
    .map(s => s.trim())
    .filter(s => s.length > 0)
    .map(s => s.endsWith('.') ? s : s + '.');

  if (steps.length === 0) steps = [data.instructions];

  return {
    id: data.id,
    title: {
      sk: data.name,
      en: data.name
    },
    image: getImageForId(data.id), 
    tags: {
      sk: data.tags,
      en: data.tags
    },
    ingredients: {
      sk: formattedIngredients,
      en: formattedIngredients
    },
    instructions: {
      sk: steps,
      en: steps
    },
    relatedRecipeIds: [], 
    calories: Math.round(data.nutrition.energy),
    protein: Math.round(data.nutrition.protein),
    carbs: Math.round(data.nutrition.carbs),
    fat: Math.round(data.nutrition.fat),
    prepTime: 30, 
    defaultPortions: data.defaultPortions
  };
};

const adaptBackendIngredient = (data: BackendIngredient): IngredientSuggestion => ({
  id: data.id.toString(),
  name: data.name,
  energy: data.energy,
  protein: data.protein,
  carbs: data.carbs,
  fat: data.fat,
  fiber: data.fiber || 0,
  sugar: data.sugar || 0
});

const fallbackData = FALLBACK_DATA as BackendRecipe[];

// 3. Fetcher Service
export const fetchRecipes = async (): Promise<{ data: Recipe[], isTestMode: boolean }> => {
  try {
    const response = await fetch(`${API_BASE_URL}/api/recipes`);
    if (!response.ok) {
      throw new Error(`API Error: ${response.statusText}`);
    }
    const backendData: BackendRecipe[] = await response.json();
    return { data: backendData.map(adaptBackendRecipe), isTestMode: false };
  } catch (error) {
    console.warn("Failed to fetch from backend, using fallback data.");
    return { data: fallbackData.map(adaptBackendRecipe), isTestMode: true };
  }
};

export const fetchIngredients = async (): Promise<IngredientSuggestion[]> => {
  try {
    const response = await fetch(`${API_BASE_URL}/api/ingredients`);
    if (!response.ok) {
      throw new Error(`API Error: ${response.statusText}`);
    }
    const data: BackendIngredient[] = await response.json();
    return data.map(adaptBackendIngredient);
  } catch (error) {
    console.warn("Failed to fetch ingredients from backend, using mock data.");
    return MOCK_INGREDIENTS;
  }
};

export const createIngredient = async (ingredient: Omit<IngredientSuggestion, 'id'>): Promise<IngredientSuggestion> => {
  try {
    const response = await fetch(`${API_BASE_URL}/api/ingredients`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(ingredient),
    });
    
    if (!response.ok) {
      throw new Error(`API Error: ${response.statusText}`);
    }
    
    const data: BackendIngredient = await response.json();
    return adaptBackendIngredient(data);
  } catch (error) {
    console.warn("Failed to create ingredient on backend, using fallback.");
    // Fallback for offline mode
    return {
      ...ingredient,
      id: `custom-${Date.now()}`
    };
  }
};

export const createRecipe = async (recipeData: any, availableIngredients: IngredientSuggestion[]): Promise<Recipe> => {
  try {
    // Construct the payload strictly according to specification
    const payload = {
      name: recipeData.title,
      instructions: recipeData.instructions.join('. '), // Flatten array to single string
      defaultPortions: recipeData.defaultPortions,
      tags: recipeData.tags,
      ingredients: recipeData.ingredients.map((ing: any) => ({
        id: parseInt(ing.ingredientId, 10), // Ensure integer ID as per spec
        quantity: ing.quantity,
        unit: ing.unit
      }))
    };

    const response = await fetch(`${API_BASE_URL}/api/recipes`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      throw new Error(`API Error: ${response.statusText}`);
    }

    // Backend returns the created recipe with calculated nutrition
    const newBackendRecipe: BackendRecipe = await response.json();
    return adaptBackendRecipe(newBackendRecipe);

  } catch (error) {
    console.warn("Failed to create recipe on backend, using fallback logic.", error);
    
    // Fallback Mock Logic
    return new Promise((resolve) => {
      setTimeout(() => {
        // 1. Calculate Nutrition
        let energy = 0;
        let protein = 0;
        let carbs = 0;
        let fat = 0;
        let fiber = 0;
        let sugar = 0;

        recipeData.ingredients.forEach((ing: any) => {
          const ref = availableIngredients.find(m => m.id === ing.ingredientId) 
                   || availableIngredients.find(m => m.name.toLowerCase() === ing.name.toLowerCase());
          
          if (ref) {
            const ratio = ing.quantity / 100;
            energy += ref.energy * ratio;
            protein += ref.protein * ratio;
            carbs += ref.carbs * ratio;
            fat += ref.fat * ratio;
            fiber += (ref.fiber || 0) * ratio;
            sugar += (ref.sugar || 0) * ratio;
          }
        });

        const portions = recipeData.defaultPortions || 1;
        
        const newBackendRecipe: BackendRecipe = {
          id: Date.now(), 
          name: recipeData.title,
          defaultPortions: portions,
          ingredients: recipeData.ingredients.map((i: any) => ({
            ingredientId: i.ingredientId || `gen-${Date.now()}-${Math.random()}`,
            name: i.name,
            quantity: i.quantity,
            unit: i.unit
          })),
          instructions: recipeData.instructions.join('. '),
          nutrition: {
            energy: energy / portions,
            protein: protein / portions,
            carbs: carbs / portions,
            fat: fat / portions,
            fiber: fiber / portions,
            sugar: sugar / portions
          },
          tags: recipeData.tags
        };

        resolve(adaptBackendRecipe(newBackendRecipe));
      }, 500);
    });
  }
};

export const fetchUserData = async (date?: string, days?: number): Promise<BackendUserData> => {
  try {
    const url = new URL(`${API_BASE_URL}/api/user-data`);
    if (date) url.searchParams.append('date', date);
    if (days) url.searchParams.append('days', days.toString());

    const response = await fetch(url.toString());
    if (!response.ok) {
      throw new Error(`API Error: ${response.statusText}`);
    }
    return await response.json();
  } catch (error) {
    console.warn("Failed to fetch user data, using default empty state.", error);
    // Default fallback
    const today = new Date();
    const offset = today.getTimezoneOffset();
    const localDate = new Date(today.getTime() - (offset * 60 * 1000));
    
    return {
      settings: {
        startDate: localDate.toISOString().split('T')[0],
        daysDuration: 7,
        language: 'sk'
      },
      inventory: [],
      plan: []
    };
  }
};

export const saveUserData = async (data: BackendUserData): Promise<boolean> => {
    try {
        const response = await fetch(`${API_BASE_URL}/api/user-data`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        if (!response.ok) throw new Error("Failed to save");
        return true;
    } catch (e) {
        // Warn instead of error to avoid red logs in console when offline
        console.warn("Save failed - Backend unavailable or network error.");
        return false;
    }
};