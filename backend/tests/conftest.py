import pytest
import os
import sys

# Add backend to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import create_app
from database import db_util, schema
from database.schema import Meal, Ingredient, MealIngredientMap, Tag, MealTagMap

@pytest.fixture
def app():
    # Create a temporary database for testing
    db_path = os.path.join(os.path.dirname(__file__), 'test.db')
    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    # Initialize the database
    with app.app_context():
        db_util.init_db()

    yield app

    # Cleanup
    if os.path.exists(db_path):
        os.remove(db_path)

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()
