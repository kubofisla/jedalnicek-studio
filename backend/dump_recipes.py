import sys
import os
import json

# Add backend to path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from main import create_app

def dump_recipes():
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

        output_file = 'all_recipes.json'
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"Successfully dumped {len(data)} recipes to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    dump_recipes()
