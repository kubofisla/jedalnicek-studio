
import { BackendPlanItem, MealPlan, Recipe } from '../types';

export const transformBackendPlanToMealPlan = (
    backendPlan: BackendPlanItem[],
    availableRecipes: Recipe[]
): MealPlan => {
    const result: MealPlan = {};

    if (!Array.isArray(backendPlan)) {
        console.warn("Backend plan is not an array:", backendPlan);
        return {};
    }

    backendPlan.forEach((item) => {
        // Find valid recipe
        const recipe = availableRecipes.find(r => r.id === item.recipeId);

        if (recipe) {
            if (!result[item.date]) {
                result[item.date] = [];
            }

            result[item.date].push({
                ...recipe,
                uid: item.uid,
                portions: item.portions,
            });
        } else {
            console.warn(`Recipe ID ${item.recipeId} not found for meal plan item ${item.uid}`);
        }
    });

    return result;
};

export const transformMealPlanToBackendPlan = (mealPlan: MealPlan): BackendPlanItem[] => {
    const backendPlan: BackendPlanItem[] = [];

    Object.entries(mealPlan).forEach(([date, meals]) => {
        meals.forEach((meal) => {
            backendPlan.push({
                uid: meal.uid,
                date: date,
                // If recipeId exists (from new meal creation), use it. 
                // Otherwise use id (from Recipe extension when loaded from backend).
                recipeId: (meal as any).recipeId || meal.id,
                portions: meal.portions
            });
        });
    });

    return backendPlan;
};
