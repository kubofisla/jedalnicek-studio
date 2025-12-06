from sqlalchemy.orm import Session
from database.db_util import get_db
from database.schema import Meal, Ingredient, MealIngredientMap, Tag, MealTagMap

def test_get_recipes_nutrition(client, app):
    with app.app_context():
        session = Session(get_db())
        
        # Clear existing data
        session.query(MealIngredientMap).delete()
        session.query(MealTagMap).delete()
        session.query(Meal).delete()
        session.query(Ingredient).delete()
        session.query(Tag).delete()
        session.commit()
        
        # Create ingredients
        i1 = Ingredient(sName="Test Ingredient 1", nEnergy=100, nFat=10, nProtein=20, nCarbohydrate=30, nSugar=5, nDietaryFiber=2)
        i2 = Ingredient(sName="Test Ingredient 2", nEnergy=200, nFat=20, nProtein=10, nCarbohydrate=40, nSugar=10, nDietaryFiber=4)
        session.add_all([i1, i2])
        session.commit()
        
        # Create meal
        meal = Meal(sName="Test Meal", sDescription="Test Description", nDefaultPortions=2)
        session.add(meal)
        session.commit()
        
        # Add ingredients to meal
        # 100g of i1 -> 100 energy
        # 50g of i2 -> 100 energy
        # Total energy = 200
        mim1 = MealIngredientMap(kMeal=meal.nId, kIngredient=i1.nId, nQuantity=100, sUnit="g")
        mim2 = MealIngredientMap(kMeal=meal.nId, kIngredient=i2.nId, nQuantity=50, sUnit="g")
        session.add_all([mim1, mim2])
        session.commit()
        
    response = client.get('/api/recipes')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    recipe = data[0]
    
    assert recipe['name'] == "Test Meal"
    assert recipe['defaultPortions'] == 2
    
    nutrition = recipe['nutrition']
    assert nutrition['energy'] == 200.0
    assert nutrition['fat'] == 20.0 # 10 + 10
    assert nutrition['protein'] == 25.0 # 20 + 5
    assert nutrition['carbohydrate'] == 50.0 # 30 + 20
    assert nutrition['sugar'] == 10.0 # 5 + 5
    assert nutrition['fiber'] == 4.0 # 2 + 2
