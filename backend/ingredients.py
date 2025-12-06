from flask import (
    Blueprint, jsonify, request
)
from database.db_util import get_db
from database.schema import Ingredient
from sqlalchemy.orm import Session
from sqlalchemy import select

bp = Blueprint('ingredients', __name__)

@bp.route('/api/ingredients', methods=['GET'])
def get_ingredients():
    db = get_db()
    
    # Use standard SQLAlchemy Core select if possible or Session
    # Using Session for consistency with other parts if present, or raw select
    # In recipes.py raw SQL was used. In user_data.py Session was used.
    # Let's use Session for clean object mapping.
    
    with Session(db) as session:
        ingredients = session.query(Ingredient).all()
        
        output = []
        for i in ingredients:
            output.append({
                'id': i.nId,
                'name': i.sName,
                'energy': float(i.nEnergy) if i.nEnergy is not None else 0,
                'fat': float(i.nFat) if i.nFat is not None else 0,
                'protein': float(i.nProtein) if i.nProtein is not None else 0,
                'carbs': float(i.nCarbohydrate) if i.nCarbohydrate is not None else 0,
                'sugar': float(i.nSugar) if i.nSugar is not None else 0,
                'fiber': float(i.nDietaryFiber) if i.nDietaryFiber is not None else 0
            })
            
    response = jsonify(output)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@bp.route('/api/ingredients', methods=['POST'])
def create_ingredient():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    if 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400
        
    db = get_db()
    with Session(db) as session:
        new_ingredient = Ingredient(
            sName=data.get('name'),
            nEnergy=data.get('energy'),
            nFat=data.get('fat'),
            nProtein=data.get('protein'),
            nCarbohydrate=data.get('carbs'),
            nSugar=data.get('sugar'),
            nDietaryFiber=data.get('fiber')
        )
        session.add(new_ingredient)
        session.commit()
        
        # Return the created ingredient ID
        return jsonify({'status': 'success', 'id': new_ingredient.nId}), 201
