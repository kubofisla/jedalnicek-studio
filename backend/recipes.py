from flask import (
    Blueprint, jsonify
)
from database.db_util import get_db
from sqlalchemy import text

bp = Blueprint('recipes', __name__)
@bp.route('/api/recipes')
def recipe_index():
    db = get_db()
    with db.connect() as conn:
        recipe_rows = conn.execute(
            text('SELECT meal.nId AS id, meal.sName AS meal, meal.sInstructions AS instructions, '
                 'meal.nDefaultPortions AS defaultPortions, '
                 'ingredient.sName AS ingredient, map.nQuantity AS quantity, map.sUnit AS unit, '
                 'ingredient.nEnergy, ingredient.nFat, ingredient.nProtein, '
                 'ingredient.nCarbohydrate, ingredient.nSugar, ingredient.nDietaryFiber, '
                 '(SELECT GROUP_CONCAT(t.sName) FROM Tag t JOIN MealTagMap mtm ON t.nId = mtm.kTag WHERE mtm.kMeal = meal.nId) AS tags '
                 'FROM meal '
                 'LEFT JOIN mealIngredientMap AS map ON map.kMeal = meal.nId '
                 'LEFT JOIN ingredient ON map.kIngredient = ingredient.nId')
        ).fetchall()

    recipes = {}
    for row in recipe_rows:
        id = row[0]

        if id not in recipes:
            #TODO:  refactor tag parsing into function
            tags_str = row[13]
            tags_list = tags_str.split(',') if tags_str else []
            recipes[id] = {
                'id' : id,
                'name' : row[1],
                'instructions' : row[2],
                'defaultPortions': row[3],
                'ingredients' : [],
                'tags': tags_list,
                'nutrition': {
                    'energy': 0,
                    'fat': 0,
                    'protein': 0,
                    'carbohydrate': 0,
                    'sugar': 0,
                    'fiber': 0
                }
            }

        # Calculate nutrition
        quantity = row[5]
        # Assuming nutrition is per 100g/ml
        ratio = quantity / 100 if quantity else 0
        
        if row[7] is not None: recipes[id]['nutrition']['energy'] += row[7] * ratio
        if row[8] is not None: recipes[id]['nutrition']['fat'] += row[8] * ratio
        if row[9] is not None: recipes[id]['nutrition']['protein'] += row[9] * ratio
        if row[10] is not None: recipes[id]['nutrition']['carbohydrate'] += row[10] * ratio
        if row[11] is not None: recipes[id]['nutrition']['sugar'] += row[11] * ratio
        if row[12] is not None: recipes[id]['nutrition']['fiber'] += row[12] * ratio

        recipes[id]['ingredients'].append({
            'ingredient' : row[4],
            'quantity' : row[5],
            'unit' : row[6],
        })

    print(recipes)
    output = list(recipes.values())
    response = jsonify(output)
    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
