from flask import (
    Blueprint, jsonify
)
from database.db_util import get_db
from sqlalchemy import text

bp = Blueprint('meals', __name__)
@bp.route('/meals')
def plan_index():
    db = get_db()
    with db.connect() as conn:
        recipe_rows = conn.execute(
            text('SELECT meal.nId AS id, meal.sName AS meal, meal.sType AS type FROM meal')
        ).fetchall()

    recipes = {}
    for row in recipe_rows:
        id = row[0]

        if id not in recipes:
            recipes[id] = {
                'id' : id,
                'name' : row[1],
                'type' : row[2]
            }

    # print(recipes)
    output = list(recipes.values())
    response = jsonify(output)
    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
