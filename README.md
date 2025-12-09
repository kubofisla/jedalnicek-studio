# MealPlanPro (Jedálniček)

A modern, responsive meal planning application built with React, allowing users to browse recipes, manage inventory, and schedule their weekly meals with automatic nutrition calculation.

## 📋 Prerequisites

- **Node.js** (v16 or higher)
- **npm** or **yarn**

## 🚀 Installation

1. **Clone the repository** (if applicable) or extract the project files.

2. **Install dependencies**
   Navigate to the project root directory and run:
   ```bash
   npm install
   ```

## 💻 Running the Application

### 1. Frontend Client
To start the React development server:

```bash
npm start
```
The application will open at `http://localhost:3000`.

### 2. Backend Server
The application is configured to communicate with a backend API at `http://localhost:5000`.

- **Full Functionality**: Ensure your backend service is running on port 5000. This enables data persistence, recipe creation, and syncing.
- **Test Mode (Fallback)**: If the backend is unreachable, the application automatically enters **Test Mode**.
  - A yellow banner will appear at the top of the screen.
  - It uses static fallback data for recipes.
  - **Note**: In Test Mode, changes (like creating a recipe or planning a meal) are tracked temporarily in the session but may not persist if the page is reloaded, as the `localStorage` logic has been replaced by backend synchronization.

## 🛠 Project Structure

- **`components/`**: Reusable UI components (RecipeCard, BigCalendar, Layout).
- **`context/`**: Global state management (`MealContext`) handling logic for plans, inventory, and settings.
- **`pages/`**: Main application views (Planner, Recipes, RecipeDetail).
- **`services/`**: API integration (`api.ts`) and mock data (`fallbackData.ts`, `mockIngredients.ts`).
- **`types.ts`**: TypeScript interfaces ensuring type safety across frontend and backend data structures.

## 🌍 Features

- **Smart Planner**: Drag-and-drop interface to schedule meals.
- **Inventory System**: Track "Meals To Do" and move them easily into your calendar.
- **Recipe Management**: Create complex recipes with automatic macro (Protein, Carbs, Fat) calculations based on ingredients.
- **Localization**: Fully localized for **Slovak (SK)** and **English (EN)**.
- **Nutrition Tracking**: Real-time daily macro summaries.

## 🔧 Troubleshooting

**"Save failed" Error:**
This indicates the backend at `localhost:5000` is offline. The app will continue to function locally, but data will not be saved to the database.

**Images not loading:**
The app uses placeholder images from Unsplash. Ensure you have an active internet connection.
