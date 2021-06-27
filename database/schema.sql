DROP TABLE IF EXISTS ingredient;
DROP TABLE IF EXISTS meal;
DROP TABLE IF EXISTS mealIngredientMapping;

CREATE TABLE ingredient (
    nId INTEGER PRIMARY KEY AUTOINCREMENT,
    sName TEXT NOT NULL,
    nEnergy INTEGER,
    nFat INTEGER,
    nProtein INTEGER,
    nCarbohydrate INTEGER,
    nSugar INTEGER,
    nDietaryFiber INTEGER
);

CREATE TABLE meal (
    nId INTEGER PRIMARY KEY AUTOINCREMENT,
    sName TEXT NOT NULL,
    sDescription TEXT NOT NULL
);

CREATE TABLE mealIngredientMapping (
    kMeal INTEGER NOT NULL,
    kIngredient INTEGER NOT NULL,
    nWeight INTEGER NOT NULL,
    sPortion TEXT,
    FOREIGN KEY(kMeal) REFERENCES meal(nId),
    FOREIGN KEY(kIngredient) REFERENCES ingredient(nId)
);