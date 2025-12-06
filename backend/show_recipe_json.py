import sys
import os
import json

# Add backend to path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from main import create_app

def show_recipe():
    app = create_app()
    client = app.test_client()
    
    try:
        response = client.get('/api/recipes')
        if response.status_code != 200:
            print(f"Error: Status code {response.status_code}")
            return

        data = response.get_json()
        if not data:
            print("Error: No data returned")
            return

        if isinstance(data, list) and len(data) > 0:
            # Print just the first recipe
            print(json.dumps(data[0], indent=2))
        else:
            print("No recipes found or unexpected data format.")
            print(json.dumps(data, indent=2))

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    show_recipe()
