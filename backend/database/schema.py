from sqlalchemy import ForeignKey, BigInteger, Numeric, Column, Identity, Integer, String
from sqlalchemy.orm import declarative_base, relationship

# CONSTANTS
MEAL_TABLE_NAME = "meal"
INGREDIENT_TABLE_NAME = "ingredient"
MI_MAP_TABLE_NAME = "mealIngredientMap"
NID = "nId"

Base = declarative_base()

class MealIngredietMap(Base):
    __tablename__ = MI_MAP_TABLE_NAME

    nKey = Column(Integer, primary_key=True)
    kMeal = Column(ForeignKey(f"{MEAL_TABLE_NAME}.{NID}"))
    kIngredient = Column(ForeignKey(f"{INGREDIENT_TABLE_NAME}.{NID}"))
    nQuantity = Column(Integer)
    sUnit = Column(String)
    ingredient = relationship("Ingredient")

class Meal(Base):
    __tablename__ = MEAL_TABLE_NAME

    nId = Column(Integer, primary_key=True)
    sName = Column(String)
    sType = Column(String)
    sDescription = Column(String)
    ingredients = relationship("MealIngredietMap")

    def __repr__(self):
        return f"Meal(id={self.nId}, name={self.sName}, description={self.sDescription})"

class Ingredient(Base):
    __tablename__ = INGREDIENT_TABLE_NAME

    nId = Column(Integer, primary_key=True)
    sName = Column(String, nullable=False)
    nEnergy = Column(Numeric)
    nFat = Column(Numeric)
    nProtein = Column(Numeric)
    nCarbohydrate = Column(Numeric)
    nSugar = Column(Numeric)
    nDietaryFiber = Column(Numeric)

    def __repr__(self):
        return f"Ingrediet(id={self.nId}, \
            name={self.sName}, \
            energy={self.nEnergy}, \
            fat={self.nFat}, \
            protein={self.nProtein}, \
            carbohydrate={self.nCarbohydrate}, \
            sugar={self.nSugar}, \
            dietary fiber={self.nDietaryFiber}, \
            )"
