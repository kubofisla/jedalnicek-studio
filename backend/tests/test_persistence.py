
import pytest
from main import create_app
from database import db_util

@pytest.fixture
def app():
    app = create_app({'TESTING': True, 'DATABASE': ':memory:'})
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

def test_persistence_cycle(client, app):
    # 1. Setup DB with default user which is required for the API
    with app.app_context():
        db_util.init_db()
        from database.schema import User, UserSettings, UserInventory, UserPlan
        from database.db_util import get_db
        from sqlalchemy.orm import Session
        
        session = Session(get_db())
        if not session.query(User).filter_by(sUsername="default").first():
            user = User(sUsername="default", sPasswordHash="x")
            session.add(user)
            session.commit()

    # 2. Mock Payload
    payload = {
        "settings": {
            "startDate": "2025-01-01",
            "daysDuration": 7,
            "language": "en"
        },
        "inventory": [],
        "plan": [
            {
                "date": "2025-01-01",
                "recipeId": 1,
                "portions": 2, 
                "uid": "test-uid-1"
            }
        ]
    }

    # 3. Save (POST)
    response = client.post('/api/user-data', json=payload)
    assert response.status_code == 200, f"Post failed: {response.data}"

    # 4. Load (GET)
    response_get = client.get('/api/user-data')
    assert response_get.status_code == 200
    data = response_get.get_json()

    # 5. Verify
    assert data['settings']['startDate'] == "2025-01-01"
    assert len(data['plan']) == 1
    item = data['plan'][0]
    assert item['uid'] == "test-uid-1"
    assert item['recipeId'] == 1
    assert item['date'] == "2025-01-01"
