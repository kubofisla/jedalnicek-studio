import { describe, it, expect } from 'vitest';
import { transformBackendPlanToMealPlan } from '../services/transformers';
import { Recipe } from '../types';

describe('User Data Parsing Integration', () => {

    // Mock Data mimicking what comes from Backend
    const mockRecipes: Recipe[] = [
        {
            id: 7,
            title: { sk: "Praženica", en: "Scrambled Eggs" },
            image: "img.jpg",
            tags: { sk: [], en: [] },
            ingredients: { sk: [], en: [] },
            instructions: { sk: [], en: [] },
            relatedRecipeIds: [],
            calories: 300,
            protein: 20,
            carbs: 5,
            fat: 25,
            prepTime: 10,
            defaultPortions: 1
        }
    ];

    const mockBackendPlan = [
        {
            "date": "2025-12-08",
            "portions": 2,
            "recipeId": 7,
            "uid": "u7hm1e29z"
        }
    ];

    it('should correctly transform flat backend plan array to date-keyed object', () => {
        const result = transformBackendPlanToMealPlan(mockBackendPlan, mockRecipes);

        // Check structure
        expect(result).toBeDefined();
        expect(result['2025-12-08']).toBeDefined();
        expect(result['2025-12-08']).toHaveLength(1);

        // Check content
        const meal = result['2025-12-08'][0];
        expect(meal.uid).toBe('u7hm1e29z');
        expect(meal.id).toBe(7); // PlannedMeal extends Recipe, so it uses 'id' from recipe
        expect(meal.portions).toBe(2);
        expect(meal.title.sk).toBe("Praženica");
    });

    it('should handle undefined or empty input gracefully', () => {
        const result = transformBackendPlanToMealPlan([], mockRecipes);
        expect(result).toEqual({});
    });

    it('should skip items with unknown recipes', () => {
        const badPlan = [{ date: '2025-01-01', recipeId: 999, portions: 1, uid: 'xxx' }];
        const result = transformBackendPlanToMealPlan(badPlan, mockRecipes);
        expect(result).toEqual({});
    });
});
