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
          "uid": "unique-id-2", # Inside month
          "recipeId": recipe_id,
          "portions": 1
        },
        {
          "date": "2024-03-31",
          "uid": "unique-id-3", # End of month
          "recipeId": recipe_id,
          "portions": 4
        },
        {
          "date": "2024-04-01",
          "uid": "unique-id-4", # Next month, but might be in range
          "recipeId": recipe_id,
          "portions": 2
        }
      ]
    }
    
    response = client.post('/api/user-data', json=payload)
    assert response.status_code == 200

    # GET Data - Legacy Month
    response = client.get('/api/user-data?month=2024-03')
    data = response.get_json()
    assert len(data['plan']) == 2 # 20 and 31
    
    # GET Data - Date and Duration (Overlap to next month)
    # Start 2024-03-25, 10 days duration -> Ends 2024-04-03
    # Should Include:
    # - All of March (2024-03-20, 2024-03-31) because start is in March
    # - AND Range 2024-03-25 to 2024-04-03 (Includes 2024-04-01)
    
    response = client.get('/api/user-data?date=2024-03-25&days=10')
    data = response.get_json()
    
    uids = [item['uid'] for item in data['plan']]
    assert "unique-id-2" in uids # In March
    assert "unique-id-3" in uids # In March
    assert "unique-id-4" in uids # In Range (Apr 1)
    assert len(data['plan']) == 3

    # GET Data - Date only (implies month of date)
    response = client.get('/api/user-data?date=2024-03-25')
    data = response.get_json()
     # Just month of March
    uids = [item['uid'] for item in data['plan']]
    assert "unique-id-2" in uids
    assert "unique-id-3" in uids
    assert "unique-id-4" not in uids
