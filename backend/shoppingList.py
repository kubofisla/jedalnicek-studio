from decimal import Decimal
from flask import (
    Blueprint, jsonify, request
)
from database.db_util import get_db

bp = Blueprint('shoppingList', __name__)
@bp.route('/shoppingList', methods = ['GET', 'POST'])
def shoppingList_index():
    recipes = request.get_json()
    db = get_db()
    ingredient_rows = db.execute(
        'SELECT meal.nId AS mealId, ingredient.nId as id, ingredient.sName AS ingredient, map.nQuantity AS quantity, map.sUnit AS unit FROM meal '
        'LEFT JOIN mealIngredientMap AS map ON map.kMeal = meal.nId '
        'LEFT JOIN ingredient ON map.kIngredient = ingredient.nId '
        'WHERE mealId in (' + ', '.join(str(recipe) for recipe in recipes) + ')'
    ).fetchall()

    multiplier = {}
    for id in recipes:
        multiplier[id] = multiplier.get(id, 0) + 1

    ingredients = {}
    for row in ingredient_rows:
        id = row['id']
        mealId = row['mealId']

        if id not in ingredients:
            ingredients[id] = {
                'id' : id,
                'name' : row['ingredient'],
                'quantity' : row['quantity'] * multiplier[mealId],
                'unit' : row['unit']
            }
        else:
            ingredients[id]['quantity'] += row['quantity'] * multiplier[mealId]

    # print(ingredients)
    output = list(ingredients.values())
    response = jsonify(output)
    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response