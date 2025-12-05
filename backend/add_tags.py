from sqlalchemy.orm import Session
from database.schema import Tag, MealTagMap, Meal
from database.db_util import get_db

def add_tags():
    session = Session(get_db())
    try:
        # Check if tags exist
        if session.query(Tag).first():
            print("Tags already exist.")
            return

        tags = {
            "vegetarian": Tag(sName="Vegetarian", sColor="#00FF00"),
            "vegan": Tag(sName="Vegan", sColor="#008000"),
            "gluten_free": Tag(sName="Gluten-Free", sColor="#FFFF00"),
            "breakfast": Tag(sName="Breakfast", sColor="#FFA500"),
            "dinner": Tag(sName="Dinner", sColor="#0000FF"),
            "lunch": Tag(sName="Lunch", sColor="#FF0000"),
        }
        session.add_all(tags.values())
        session.commit()
        
        # Assign tags to meals
        meal = session.query(Meal).filter(Meal.sName == "Rýžové placičky s jablkem a banánem").first()
        if meal:
            meal.tags.append(MealTagMap(tag=tags["breakfast"]))
            meal.tags.append(MealTagMap(tag=tags["vegetarian"]))
            meal.tags.append(MealTagMap(tag=tags["gluten_free"]))
            
        meal = session.query(Meal).filter(Meal.sName == "Osvěžující borůvkový bowl").first()
        if meal:
            meal.tags.append(MealTagMap(tag=tags["breakfast"]))
            meal.tags.append(MealTagMap(tag=tags["vegetarian"]))
            
        session.commit()
        print("Tags added successfully.")
    except Exception as e:
        print(f"Error adding tags: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    add_tags()
