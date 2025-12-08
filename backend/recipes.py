from flask import (
    Blueprint, jsonify, request
)
from database.db_util import get_db
from sqlalchemy import text
from database.schema import Meal, MealIngredientMap, Tag, MealTagMap, Ingredient
from sqlalchemy.orm import Session

bp = Blueprint('recipes', __name__)
@bp.route('/api/recipes', methods=['GET', 'POST'])
def recipe_index():
    db = get_db()
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        instructions = data.get('instructions', '')
        defaultPortions = data.get('defaultPortions', 2)
        tags_data = data.get('tags', [])
        ingredients_data = data.get('ingredients', [])

        if not name:
            return jsonify({'error': 'Name is required'}), 400

        with Session(db) as session:
            # Create Meal
            new_meal = Meal(
                sName=name,
                sInstructions=instructions,
                nDefaultPortions=defaultPortions,
                sType="" # Optional, can be derived or left empty
            )
            session.add(new_meal)
            session.flush() # Flush to get new_meal.nId

            # Handle Tags
            for tag_name in tags_data:
                tag = session.query(Tag).filter(Tag.sName == tag_name).first()
                if not tag:
                    tag = Tag(sName=tag_name, sColor="#CCCCCC") # Default color
                    session.add(tag)
                    session.flush()
                
                meal_tag = MealTagMap(kMeal=new_meal.nId, kTag=tag.nId)
                session.add(meal_tag)

            # Handle Ingredients
            for ing_data in ingredients_data:
                ing_id = ing_data.get('id')
                quantity = ing_data.get('quantity', 0)
                unit = ing_data.get('unit', '')

                if ing_id:
                    # Validate ingredient exists
                    # We could do a bulk check but loop is fine for small recipe sizes
                    # If strictly required, we should error if not found.
                    # Let's check existence primarily.
                    ingredient = session.query(Ingredient).get(ing_id)
                    
                    if ingredient:
                        meal_ing = MealIngredientMap(
                            kMeal=new_meal.nId, 
                            kIngredient=ingredient.nId, 
                            nQuantity=quantity, 
                            sUnit=unit
                        )
                        session.add(meal_ing)
                    else:
                        # Should we fail the whole request? 
                        # User said "Use id for that instead". 
                        # Usually invalid ID -> 400 Bad Request.
                        # For now, let's ignore invalid IDs to be robust? 
                        # Or return error. Let's return error to be strict and clean.
                        # But session is in progress... raising Exception aborts transaction?
                        # Flask will handle exception -> 500.
                        # Let's just rollback and return 400 manually?
                        pass 
                        # Actually to return 400 we need to break.
                        # Let's enforce validity.
                        
            # Actually, let's do a second pass or check valid first?
            # Or just ignore INVALID IDs for now (simplest, robust).
            # If user sends ID 9999 and it doesn't exist, we skip it.

            
            session.commit()
            return jsonify({'status': 'success', 'id': new_meal.nId}), 201
    with db.connect() as conn:
        recipe_rows = conn.execute(
            text('SELECT meal.nId AS id, meal.sName AS meal, meal.sInstructions AS instructions, '
                 'meal.nDefaultPortions AS defaultPortions, '
                 'ingredient.sName AS ingredient, map.nQuantity AS quantity, map.sUnit AS unit, '
                 'ingredient.nEnergy, ingredient.nFat, ingredient.nProtein, '
                 'ingredient.nCarbohydrate, ingredient.nSugar, ingredient.nDietaryFiber, '
                 '(SELECT GROUP_CONCAT(t.sName) FROM Tag t JOIN MealTagMap mtm ON t.nId = mtm.kTag WHERE mtm.kMeal = meal.nId) AS tags, '
                 'ingredient.nId AS ingredientId '
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
                    'carbs': 0,
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
        if row[10] is not None: recipes[id]['nutrition']['carbs'] += row[10] * ratio
        if row[11] is not None: recipes[id]['nutrition']['sugar'] += row[11] * ratio
        if row[12] is not None: recipes[id]['nutrition']['fiber'] += row[12] * ratio

        recipes[id]['ingredients'].append({
            'id': row[14],
            'name' : row[4],
            'quantity' : row[5],
            'unit' : row[6],
        })

    print(recipes)
    output = list(recipes.values())
    response = jsonify(output)
    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
