from sqlalchemy.orm import Session
from database.db_util import get_db
from database.schema import Ingredient

def test_get_ingredients(client, app):
    with app.app_context():
        session = Session(get_db())
        # Clear existing ingredients
        session.query(Ingredient).delete()
        
        i1 = Ingredient(sName="Test Ing 1", nEnergy=100, nCarbohydrate=50)
        session.add(i1)
        session.commit()

    response = client.get('/api/ingredients')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]['name'] == "Test Ing 1"
    assert data[0]['energy'] == 100.0
    assert data[0]['carbs'] == 50.0  # Verify 'carbs' usage

def test_create_ingredient(client, app):
    payload = {
        "name": "New Ingredient",
        "energy": 200,
        "fat": 10.5,
        "carbs": 30
    }
    
    response = client.post('/api/ingredients', json=payload)
    assert response.status_code == 201
    data = response.get_json()
    assert data['status'] == 'success'
    assert 'id' in data
    
    # Verify persistence
    with app.app_context():
        session = Session(get_db())
        ing = session.query(Ingredient).filter(Ingredient.nId == data['id']).first()
        assert ing is not None
        assert ing.sName == "New Ingredient"
        assert ing.nEnergy == 200.0
        assert ing.nFat == 10.5
        assert ing.nCarbohydrate == 30.0

def test_create_ingredient_validation(client):
    payload = {
        "energy": 200
    }
    response = client.post('/api/ingredients', json=payload)
    assert response.status_code == 400
    assert response.get_json()['error'] == 'Name is required'
