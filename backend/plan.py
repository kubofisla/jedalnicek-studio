from flask import (
    Blueprint, jsonify
)
from database.schema import PlanGroup, Plan
from database.db_util import get_db
from sqlalchemy.sql import select
from sqlalchemy.orm import Session

def getOrDefault(obj, default):
    if obj == None:
        return default
    else:
        return obj

bp = Blueprint('plan', __name__)
@bp.route('/api/plan')
def plan_index():
    db = get_db()
    # recipe_rows = db.execute(
    #     'SELECT meal.nId AS id, meal.sName AS meal, meal.sType AS type FROM meal'
    # ).fetchall()

    conn = db.connect()
    result = select(PlanGroup, Plan)
    recipe_rows = conn.execute(result)
    session = Session(db)
    recipe_rows = session.query(PlanGroup, Plan).filter(PlanGroup.nId == Plan.kGroup).all()

    planGroup = {}
    for group, plan in recipe_rows:
        id = group.nId
        if id not in planGroup:
            planGroup[id] = {
                'id' : id,
                'name' : group.sName,
                'inputs' : []
            }

        planGroup[id]['inputs'].append({
            'id' : plan.nId,
            'name' : plan.sName,
            'meal' : getOrDefault(plan.kMeal, plan.sCustomValue)
        })

    # print(str(planGroup.values()))
    output = list(planGroup.values())
    response = jsonify(output)
    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
