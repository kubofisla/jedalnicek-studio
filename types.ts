export type Language = 'sk' | 'en';

export interface LocalizedContent<T> {
  sk: T;
  en: T;
}

export interface Recipe {
  id: number;
  title: LocalizedContent<string>;
  image: string;
  tags: LocalizedContent<string[]>;
  ingredients: LocalizedContent<string[]>;
  instructions: LocalizedContent<string[]>;
  relatedRecipeIds: number[];
  calories: number; // per portion
  protein: number; // in grams per portion
  carbs: number;   // in grams per portion
  fat: number;     // in grams per portion
  prepTime: number; // in minutes
  defaultPortions: number;
}

export interface PlannedMeal extends Recipe {
  uid: string;
  portions: number;
}

export interface InventoryItem {
  uid: string;
  recipeId: number;
  portions: number;
}

export type MealPlan = Record<string, PlannedMeal[]>; // Key is YYYY-MM-DD

export interface AppSettings {
  startDate: string; // YYYY-MM-DD
  daysDuration: number;
  language: Language;
}

export interface IngredientSuggestion {
  id: string;
  name: string;
  energy: number; // kcal per 100g
  protein: number;
  carbs: number;
  fat: number;
  fiber?: number;
  sugar?: number;
}

// --- Backend Data Types ---

export interface BackendPlanItem {
  uid: string;
  date: string;
  recipeId: number;
  portions: number;
}

export interface BackendInventoryItem {
  uid: string;
  recipeId: number;
  portions: number;
}

export interface BackendUserData {
  settings: AppSettings;
  inventory: BackendInventoryItem[];
  plan: BackendPlanItem[];
}

export interface MealContextType {
  recipes: Recipe[];
  plan: MealPlan;
  inventory: InventoryItem[]; 
  settings: AppSettings;
  availableIngredients: IngredientSuggestion[];
  updateSettings: (newSettings: Partial<AppSettings>) => void;
  addMealToDay: (date: string, recipe: Recipe, portions?: number) => void;
  removeMealFromDay: (date: string, uid: string) => void;
  updateMealPortions: (date: string, uid: string, change: number) => void;
  toggleInventory: (recipeId: number) => void;
  updateInventoryPortions: (uid: string, change: number) => void;
  consumeInventoryPortions: (uid: string, amount: number) => void;
  removeFromInventory: (uid: string) => void;
  createRecipe: (data: any) => Promise<Recipe>;
  addIngredient: (ingredient: Omit<IngredientSuggestion, 'id'>) => Promise<IngredientSuggestion>;
  t: (key: any) => string;
  language: Language;
  isTestMode: boolean;
  saveError: boolean;
}