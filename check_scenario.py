
import requests
import json
import time

BASE_URL = "http://localhost:5000/api/user-data"

def run():
    print("--- Step 0: Get Initial State (Checking if backend is up) ---")
    try:
        r0 = requests.get(BASE_URL)
        if r0.status_code != 200:
            print(f"Failed to connect: {r0.status_code}")
            return
    except Exception as e:
        print(f"Connection failed: {e}")
        return

    data0 = r0.json()
    print(f"Initial Plan Items: {len(data0.get('plan', []))}")

    # Fetch recipes to get valid ID
    r_recipes = requests.get("http://localhost:5000/api/recipes")
    recipes = r_recipes.json()
    if not recipes:
        print("No recipes found! Cannot add meal.")
        return
    valid_recipe_id = recipes[0]['id']

    # 4. Add Meal 1 (Day 1)
    print("\n--- Step 1: Add Meal 1 ---")
    meal1 = {
        "date": "2025-01-01",
        "recipeId": valid_recipe_id,
        "portions": 1,
        "uid": "debug-uid-1"
    }
    
    current_plan = [meal1]
    
    payload1 = {
        "settings": data0.get('settings', {}),
        "inventory": data0.get('inventory', []),
        "plan": current_plan
    }
    
    print("Sending POST 1...")
    r1 = requests.post(BASE_URL, json=payload1)
    print(f"POST 1 Status: {r1.status_code}")
    if r1.status_code != 200:
        print(f"Error Response: {r1.text}")
    
    # 5. Refresh (GET)
    print("\n--- Step 2: Refresh (GET) ---")
    r2 = requests.get(BASE_URL)
    data2 = r2.json()
    plan2 = data2.get('plan', [])
    print(f"Plan Items after Refresh 1: {len(plan2)}")
    
    for p in plan2:
        print(f" - Found Item: {p.get('uid')}")

    if len(plan2) == 0:
        print("FAIL: Meal 1 was not saved.")
    else:
        print("SUCCESS: Meal 1 saved.")

if __name__ == "__main__":
    run()
