# Meal Companion Backend API Documentation

**Created Date:** 2025-12-07
**Commit Hash:** `9d185f4d19c8c34100b680b4dcbdbaf0d7a050ff`

## Overview

This documentation provides a comprehensive guide to the API endpoints exposed by the Meal Companion backend.

The API is built using Flask.

## Endpoints

### 1. Recipes

#### GET `/api/recipes`
Retrieves a detailed list of all recipes.

**Response:**
```json
[
  {
    "id": 1,
    "name": "Recipe Name",
    "instructions": "Step by step instructions...",
    "defaultPortions": 2,
    "tags": ["Tag1", "Tag2"],
    "nutrition": {
      "energy": 500.0,
      "fat": 20.0,
      "protein": 15.0,
      "carbs": 60.0,
      "sugar": 5.0,
      "fiber": 8.0
    },
    "ingredients": [
      {
        "ingredient": "Ingredient Name",
        "quantity": 100,
        "unit": "g"
      }
    ]
  }
]
```

**Field Descriptions:**

| Field | Type | Description |
|---|---|---|
| `id` | Integer | Unique identifier for the recipe. |
| `name` | String | Name of the recipe. |
| `instructions` | String | Step-by-step instructions. |
| `defaultPortions` | Integer | Default number of portions the recipe produces. |
| `tags` | Array<String> | List of tags associated with the recipe (e.g., "Breakfast", "Vegan"). |
| `nutrition` | Object | Calculated total nutrition per 1 portion (approximate). |
| `nutrition.energy` | Float | Energy in kCal. |
| `nutrition.carbs` | Float | Carbohydrates in grams. |
| `nutrition.protein` | Float | Protein in grams. |
| `nutrition.fat` | Float | Fat in grams. |
| `nutrition.sugar` | Float | Sugar in grams. |
| `nutrition.fiber` | Float | Dietary fiber in grams. |
| `ingredients` | Array<Object> | List of ingredients needed for the recipe. |
| `ingredients[].ingredient` | String | Name of the ingredient. |
| `ingredients[].quantity` | Float | Quantity required. |
| `ingredients[].unit` | String | Unit of measurement (e.g., "g", "ml", "pcs"). |

### 2. Ingredients

#### GET `/api/ingredients`
Retrieves a list of all available ingredients.

**Response:**
```json
[
  {
    "id": 1,
    "name": "Rice",
    "energy": 350.0,
    "fat": 0.5,
    "protein": 7.0,
    "carbs": 78.0,
    "sugar": 0.1,
    "fiber": 1.0
  }
]
```

**Field Descriptions:**

| Field | Type | Description |
|---|---|---|
| `id` | Integer | Unique identifier for the ingredient. |
| `name` | String | Name of the ingredient. |
| `energy` | Float | Energy (kCal) per 100g/ml. |
| `fat` | Float | Fat (g) per 100g/ml. |
| `protein` | Float | Protein (g) per 100g/ml. |
| `carbs` | Float | Carbohydrates (g) per 100g/ml. |
| `sugar` | Float | Sugar (g) per 100g/ml. |
| `fiber` | Float | Dietary fiber (g) per 100g/ml. |

#### POST `/api/ingredients`
Creates a new ingredient.

**Request Body:**
```json
{
  "name": "New Ingredient",
  "energy": 200,
  "fat": 10,
  "protein": 5,
  "carbs": 20,
  "sugar": 2,
  "fiber": 3
}
```
*Note: `name` is required. Nutritional values are optional (default to 0).*

**Response:**
```json
{
  "status": "success",
  "id": 123
}
```

### 3. User Data (Sync)

#### GET `/api/user-data`
Retrieves user settings, inventory, and meal plan.

**Parameters:**
- `date` (optional): Start date validation for the plan query (YYYY-MM-DD). Use with `days`.
- `days` (optional): Number of days to include in the plan query range.
- `month` (optional, legacy): Filter plan by specific month (YYYY-MM).

**Logic:**
If `date` and `days` are provided, the response includes plan items for:
1. The entire month of the requested `date`.
2. The specific date range `[date, date + days - 1]`.

**Response:**
```json
{
  "settings": {
    "startDate": "2024-03-20",
    "daysDuration": 7,
    "language": "en"
  },
  "inventory": [
    {
      "uid": "uid-string",
      "recipeId": 10,
      "portions": 2
    }
  ],
  "plan": [
    {
      "uid": "uid-string",
      "date": "2024-03-20",
      "recipeId": 3,
      "portions": 4
    }
  ]
}
```

#### POST `/api/user-data`
Persists user data.

**Request Body:**
```json
{
  "settings": {
    "startDate": "2024-03-20",
    "daysDuration": 7,
    "language": "en"
  },
  "inventory": [ ... ],
  "plan": [ ... ]
}
```
*Note: Inventory items for the user are replaced. Plan items are upserted by UID.*

**Field Descriptions (User Data Object):**

| Section | Field | Type | Description |
|---|---|---|---|
| **settings** | `startDate` | String | Start date of the current plan (YYYY-MM-DD). |
| | `daysDuration` | Integer | Duration of the plan in days. |
| | `language` | String | User's preferred language (e.g., "en", "sk"). |
| **inventory** | `uid` | String | Unique Client-side ID for the inventory item (for UI tracking). |
| | `recipeId` | Integer | ID of the recipe in the inventory. |
| | `portions` | Integer | Number of portions available. |
| **plan** | `uid` | String | Unique Client-side ID for the plan item (used for upserts). |
| | `date` | String | Date assigned for this meal (YYYY-MM-DD). |
| | `recipeId` | Integer | ID of the recipe planned. |
| | `portions` | Integer | Number of portions planned. |

