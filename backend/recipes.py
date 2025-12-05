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
            text('SELECT meal.nId AS id, meal.sName AS meal, meal.sDescription AS description, ingredient.sName AS ingredient, map.nQuantity AS quantity, map.sUnit AS unit, '
            '(SELECT GROUP_CONCAT(t.sName) FROM Tag t JOIN MealTagMap mtm ON t.nId = mtm.kTag WHERE mtm.kMeal = meal.nId) AS tags '
            'FROM meal '
            'LEFT JOIN mealIngredientMap AS map ON map.kMeal = meal.nId '
            'LEFT JOIN ingredient ON map.kIngredient = ingredient.nId')
        ).fetchall()

    recipes = {}
    for row in recipe_rows:
        id = row[0]

        if id not in recipes:
            tags_str = row[6]
            tags_list = tags_str.split(',') if tags_str else []
            recipes[id] = {
                'id' : id,
                'name' : row[1],
                'description' : row[2],
                'ingredients' : [],
                'tags': tags_list
            }

        recipes[id]['ingredients'].append({
            'ingredient' : row[3],
            'quantity' : row[4],
            'unit' : row[5],
        })

    print(recipes)
    output = list(recipes.values())
    response = jsonify(output)
    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
