
import { adaptBackendRecipe, adaptBackendIngredient, BackendRecipe, BackendIngredient } from '../services/api';
// We need to fetch from the actual running backend
// Since we are in a node environment, we might need to rely on the global fetch if node version is > 18
// or import it. Assuming node 20+ based on context or that users env has it.

const BASE_URL = 'http://localhost:5000';

async function runTests() {
    console.log('Starting integration tests for adapters...');

    let failures = 0;

    // --- Test Recipes ---
    try {
        console.log(`Fetching recipes from ${BASE_URL}/api/recipes...`);
        const response = await fetch(`${BASE_URL}/api/recipes`);

        if (!response.ok) {
            throw new Error(`Failed to fetch recipes: ${response.status} ${response.statusText}`);
        }

        const backendRecipes: BackendRecipe[] = await response.json();
        console.log(`Fetched ${backendRecipes.length} recipes.`);

        backendRecipes.forEach((bRecipe, index) => {
            try {
                const recipe = adaptBackendRecipe(bRecipe);

                // Assertions
                if (typeof recipe.id !== 'number') throw new Error('ID is not a number');
                if (!recipe.title.sk) throw new Error('Title SK is missing');
                if (!recipe.title.en) throw new Error('Title EN is missing');
                if (!Array.isArray(recipe.tags.sk)) throw new Error('Tags SK is not an array');
                if (!Array.isArray(recipe.ingredients.sk)) throw new Error('Ingredients SK is not an array');
                if (!Array.isArray(recipe.instructions.sk)) throw new Error('Instructions SK is not an array');
                if (!Array.isArray(recipe.tags.en)) throw new Error('Tags EN is not an array');
                if (!Array.isArray(recipe.ingredients.en)) throw new Error('Ingredients EN is not an array');
                if (!Array.isArray(recipe.instructions.en)) throw new Error('Instructions EN is not an array');
                if (!recipe.defaultPortions) throw new Error('Default Portions is missing');
                if (recipe.ingredients.sk.length > 0) {
                    if (!recipe.ingredients.sk[0].amount) throw new Error('Ingredient amount is missing');
                    if (!recipe.ingredients.sk[0].name) throw new Error('Ingredient name is missing');
                }
                if (recipe.instructions.sk.length > 0) {
                    if (!recipe.instructions.sk[0]) throw new Error('Instruction is missing');
                }

                if (typeof recipe.calories !== 'number' || isNaN(recipe.calories)) throw new Error(`Calories is invalid: ${recipe.calories}`);
                if (typeof recipe.protein !== 'number' || isNaN(recipe.protein)) throw new Error(`Protein is invalid: ${recipe.protein}`);
                if (typeof recipe.carbs !== 'number' || isNaN(recipe.carbs)) throw new Error(`Carbs is invalid: ${recipe.carbs}`);
                if (typeof recipe.fat !== 'number' || isNaN(recipe.fat)) throw new Error(`Fat is invalid: ${recipe.fat}`);
                if (typeof recipe.defaultPortions !== 'number' || isNaN(recipe.defaultPortions)) throw new Error(`DefaultPortions is invalid: ${recipe.defaultPortions}`);

                // Check for undefined values in critical fields
                if (recipe.title.sk === undefined) throw new Error('Title SK is undefined');

            } catch (e: any) {
                console.error(`[FAIL] Recipe at index ${index} (ID: ${bRecipe.id}): ${e.message}`);
                failures++;
            }
        });

    } catch (e: any) {
        console.error(`[FATAL] Failed to test recipes: ${e.message}`);
        failures++;
    }

    // --- Test Ingredients ---
    try {
        console.log(`Fetching ingredients from ${BASE_URL}/api/ingredients...`);
        const response = await fetch(`${BASE_URL}/api/ingredients`);

        if (!response.ok) {
            throw new Error(`Failed to fetch ingredients: ${response.status} ${response.statusText}`);
        }

        const backendIngredients: BackendIngredient[] = await response.json();
        console.log(`Fetched ${backendIngredients.length} ingredients.`);

        backendIngredients.forEach((bIngredient, index) => {
            try {
                const ingredient = adaptBackendIngredient(bIngredient);

                // Assertions
                if (!ingredient.id) throw new Error('ID is missing');
                if (!ingredient.name) throw new Error('Name is missing');

                if (typeof ingredient.energy !== 'number' || isNaN(ingredient.energy)) throw new Error(`Energy is invalid: ${ingredient.energy}`);
                if (typeof ingredient.protein !== 'number' || isNaN(ingredient.protein)) throw new Error(`Protein is invalid: ${ingredient.protein}`);
                if (typeof ingredient.carbs !== 'number' || isNaN(ingredient.carbs)) throw new Error(`Carbs is invalid: ${ingredient.carbs}`);
                if (typeof ingredient.fat !== 'number' || isNaN(ingredient.fat)) throw new Error(`Fat is invalid: ${ingredient.fat}`);

            } catch (e: any) {
                console.error(`[FAIL] Ingredient at index ${index} (ID: ${bIngredient.id}): ${e.message}`);
                failures++;
            }
        });

    } catch (e: any) {
        console.error(`[FATAL] Failed to test ingredients: ${e.message}`);
        failures++;
    }

    if (failures === 0) {
        console.log('SUCCESS: All tests passed!');
    } else {
        console.error(`FAILURE: ${failures} issues found.`);
        process.exit(1);
    }
}

runTests();
