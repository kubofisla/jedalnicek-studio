import pytest
from database.schema import Meal, Tag, MealIngredientMap, Ingredient, MealTagMap
from sqlalchemy.orm import Session
from database.db_util import get_db

def test_create_recipe(client, app):
    with app.app_context():
        # Clean up
        session = Session(get_db())
        session.query(MealIngredientMap).delete()
        session.query(MealTagMap).delete()
        session.query(Meal).delete()
        session.query(Ingredient).delete()
        session.query(Tag).delete()
        session.commit()

        # Create ingredient beforehand? Or let API create it.
        # Let's verify API creates it if missing. -- OLD LOGIC
        # NEW LOGIC: Must exist.
        ing = Ingredient(sName="Test Ingredient", nEnergy=100)
        session.add(ing)
        session.commit()
        ing_id = ing.nId
        
    payload = {
        "name": "New Test Recipe",
        "instructions": "Mix everything.",
        "defaultPortions": 4,
        "tags": ["Dinner", "Spicy"],
        "ingredients": [
            {
                "id": ing_id,
                "quantity": 100,
                "unit": "g"
            }
        ]
    }

    response = client.post('/api/recipes', json=payload)
    assert response.status_code == 201
    data = response.get_json()
    assert data['status'] == 'success'
    assert 'id' in data
    new_id = data['id']

    with app.app_context():
        session = Session(get_db())
        meal = session.query(Meal).get(new_id)
        assert meal is not None
        assert meal.sName == "New Test Recipe"
        assert meal.nDefaultPortions == 4
        
        # Verify Tags
        assert len(meal.tags) == 2
        tag_names = [t.tag.sName for t in meal.tags]
        assert "Dinner" in tag_names
        assert "Spicy" in tag_names

        # Verify Ingredients
        assert len(meal.ingredients) == 1
        ing_map = meal.ingredients[0]
        assert ing_map.ingredient.sName == "Test Ingredient"
        assert ing_map.nQuantity == 100
        assert ing_map.sUnit == "g"

def test_create_recipe_missing_name(client):
    payload = {
        "instructions": "No name recipe"
    }
    response = client.post('/api/recipes', json=payload)
    assert response.status_code == 400
    assert response.get_json()['error'] == 'Name is required'
