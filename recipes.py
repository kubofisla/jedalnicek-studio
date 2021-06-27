import functools

from flask import (
    Blueprint, render_template
)
from database.db import get_db

bp = Blueprint('recipes', __name__)

@bp.route('/')
def recipe_index():
    db = get_db()
    recipe_rows = db.execute(
        'SELECT meal.nId AS id, meal.sName AS meal, meal.sDescription AS description, ingredient.sName AS ingredient, map.nQuantity AS quantity, map.sUnit AS unit FROM meal '
        'LEFT JOIN mealIngredientMapping AS map ON map.kMeal = meal.nId '
        'LEFT JOIN ingredient ON map.kIngredient = ingredient.nId'
    ).fetchall()

    recipes = {}
    for row in recipe_rows:
        id = row['id']
        
        if id not in recipes:
            recipes[id] = {
                'meal' : row['meal'],
                'description' : row['description'],
                'ingredients' : []
            }

        recipes[id]['ingredients'].append({
            'ingredient' : row["ingredient"],
            'quantity' : row["quantity"],
            'unit' : row["unit"],
        })

    return render_template('recipe_index.html', recipes=recipes.values())