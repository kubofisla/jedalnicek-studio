from sqlalchemy.orm import Session
from database.db_util import get_db
from database.schema import User, UserSettings, UserInventory, UserPlan, Meal

def test_user_data_flow(client, app):
    with app.app_context():
        session = Session(get_db())
        
        # Setup Default User
        if not session.query(User).filter(User.sUsername == "default").first():
            user = User(sUsername="default")
            session.add(user)
            session.commit()
            
        # Create a dummy recipe
        meal = Meal(sName="Test Recipe", nDefaultPortions=2)
        session.add(meal)
        session.commit()
        recipe_id = meal.nId

    # POST Data
    payload = {
      "settings": {
        "startDate": "2024-03-20",
        "daysDuration": 7,
        "language": "en"
      },
      "inventory": [
        {
          "uid": "unique-id-1",
          "recipeId": recipe_id,
          "portions": 2
        }
      ],
      "plan": [
        {
          "date": "2024-03-20",
          "uid": "unique-id-2",
          "recipeId": recipe_id,
          "portions": 1
        },
        {
          "date": "2024-03-21",
          "uid": "unique-id-3",
          "recipeId": recipe_id,
          "portions": 4
        }
      ]
    }
    
    response = client.post('/api/user-data', json=payload)
    assert response.status_code == 200
    assert response.get_json()['status'] == 'success'

    # GET Data
    response = client.get('/api/user-data?month=2024-03')
    assert response.status_code == 200
    data = response.get_json()
    
    assert data['settings']['startDate'] == "2024-03-20"
    assert data['settings']['daysDuration'] == 7
    assert data['settings']['language'] == "en"
    
    assert len(data['inventory']) == 1
    assert data['inventory'][0]['uid'] == "unique-id-1"
    assert data['inventory'][0]['portions'] == 2
    
    assert len(data['plan']) == 2
    # Verify filtering
    response = client.get('/api/user-data?month=2024-04')
    data_apr = response.get_json()
    assert len(data_apr['plan']) == 0
