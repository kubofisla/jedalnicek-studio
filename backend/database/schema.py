from sqlalchemy import ForeignKey, Numeric, Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship

# CONSTANTS
MEAL_TABLE_NAME = "Meal"
INGREDIENT_TABLE_NAME = "Ingredient"
M_I_MAP_TABLE_NAME = "MealIngredientMap"
NID = "nId"
PLAN_TABLE_NAME = "Plan"
PLAN_GROUP_TABLE_NAME = "PlanGroup"
TAG_TABLE_NAME = "Tag"
M_T_MAP_TABLE_NAME = "MealTagMap"
USER_TABLE_NAME = "User"
USER_SETTINGS_TABLE_NAME = "UserSettings"
USER_INVENTORY_TABLE_NAME = "UserInventory"
USER_PLAN_TABLE_NAME = "UserPlan"

Base = declarative_base()

class MealIngredientMap(Base):
    __tablename__ = M_I_MAP_TABLE_NAME

    nKey = Column(Integer, primary_key=True)
    kMeal = Column(ForeignKey(f"{MEAL_TABLE_NAME}.{NID}"))
    kIngredient = Column(ForeignKey(f"{INGREDIENT_TABLE_NAME}.{NID}"))
    nQuantity = Column(Integer)
    sUnit = Column(String)
    ingredient = relationship(INGREDIENT_TABLE_NAME)

class Meal(Base):
    __tablename__ = MEAL_TABLE_NAME

    nId = Column(Integer, primary_key=True)
    sName = Column(String)
    sType = Column(String)
    sInstructions = Column(String)
    nDefaultPortions = Column(Integer, default=2)
    ingredients = relationship(M_I_MAP_TABLE_NAME)
    tags = relationship(M_T_MAP_TABLE_NAME)
    
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

class Plan(Base):
    __tablename__ = PLAN_TABLE_NAME

    nId = Column(Integer, primary_key=True)
    kGroup = Column(Integer, ForeignKey(f"{PLAN_GROUP_TABLE_NAME}.{NID}"))
    kMeal = Column(Integer, ForeignKey(f"{MEAL_TABLE_NAME}.{NID}"))
    sName = Column(String, nullable=False)
    group = relationship(PLAN_GROUP_TABLE_NAME)
    meal = relationship(MEAL_TABLE_NAME)
    sCustomValue = Column(String)
    # nOrder = Column(Integer)

class PlanGroup(Base):
    __tablename__ = PLAN_GROUP_TABLE_NAME

    nId = Column(Integer, primary_key=True)
    sName = Column(String, nullable=False)
    kGroup = Column(Integer, ForeignKey(f"{PLAN_GROUP_TABLE_NAME}.{NID}"))
    # plans = relationship(PLAN_TABLE_NAME)
    # group = relationship(PLAN_GROUP_TABLE_NAME)
    # nOrder = Column(Integer, nullable=False, unique=True)


class MealTagMap(Base):
    __tablename__ = M_T_MAP_TABLE_NAME

    nKey = Column(Integer, primary_key=True)
    kMeal = Column(ForeignKey(f"{MEAL_TABLE_NAME}.{NID}"))
    kTag = Column(ForeignKey(f"{TAG_TABLE_NAME}.{NID}"))
    tag = relationship(TAG_TABLE_NAME)

class Tag(Base):
    __tablename__ = TAG_TABLE_NAME

    nId = Column(Integer, primary_key=True)
    sName = Column(String, nullable=False, unique=True)
    sColor = Column(String)

class User(Base):
    __tablename__ = USER_TABLE_NAME

    nId = Column(Integer, primary_key=True)
    sUsername = Column(String, unique=True, nullable=False)

class UserSettings(Base):
    __tablename__ = USER_SETTINGS_TABLE_NAME

    nId = Column(Integer, primary_key=True)
    kUser = Column(ForeignKey(f"{USER_TABLE_NAME}.{NID}"))
    sStartDate = Column(String)
    nDaysDuration = Column(Integer)
    sLanguage = Column(String)

class UserInventory(Base):
    __tablename__ = USER_INVENTORY_TABLE_NAME

    nId = Column(Integer, primary_key=True)
    kUser = Column(ForeignKey(f"{USER_TABLE_NAME}.{NID}"))
    sUid = Column(String)
    kRecipe = Column(ForeignKey(f"{MEAL_TABLE_NAME}.{NID}"))
    nPortions = Column(Integer)

class UserPlan(Base):
    __tablename__ = USER_PLAN_TABLE_NAME

    nId = Column(Integer, primary_key=True)
    kUser = Column(ForeignKey(f"{USER_TABLE_NAME}.{NID}"))
    sDate = Column(String)
    sUid = Column(String)
    kRecipe = Column(ForeignKey(f"{MEAL_TABLE_NAME}.{NID}"))
    nPortions = Column(Integer)
