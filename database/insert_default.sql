-- TESTOVACIE DATA

INSERT INTO meal (sName, sDescription)
VALUES("Poradnej knedlik s poradnym masem", "Toto je navod na pripravu. Naloz knedlik, naloz maso");

INSERT INTO ingredient (sName, nEnergy)
VALUES("Ingrediencia", "512");

--TODO Tato mapa sa asi musi vytvarat nejak ingelignetnejsie, toto je guessujem hodnoty to je naprd
INSERT INTO mealIngredientMapping (kMeal, kIngredient, nQuantity, sUnit)
VALUES("1", "1", 100, "g");