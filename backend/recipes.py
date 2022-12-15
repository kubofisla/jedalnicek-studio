from flask import (
    Blueprint, jsonify
)
from database.db_util import get_db

bp = Blueprint('recipes', __name__)
@bp.route('/recipes')
def recipe_index():
    db = get_db()
    recipe_rows = db.execute(
        'SELECT meal.nId AS id, meal.sName AS meal, meal.sDescription AS description, ingredient.sName AS ingredient, map.nQuantity AS quantity, map.sUnit AS unit FROM meal '
        'LEFT JOIN mealIngredientMap AS map ON map.kMeal = meal.nId '
        'LEFT JOIN ingredient ON map.kIngredient = ingredient.nId'
    ).fetchall()

    recipes = {}
    for row in recipe_rows:
        id = row['id']

        if id not in recipes:
            recipes[id] = {
                'id' : id,
                'name' : row['meal'],
                'description' : row['description'],
                'ingredients' : []
            }

        recipes[id]['ingredients'].append({
            'ingredient' : row["ingredient"],
            'quantity' : row["quantity"],
            'unit' : row["unit"],
        })

    print(recipes)
    output = list(recipes.values())
    response = jsonify(output)
    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
