import React from 'react';
import { HashRouter, Routes, Route, Navigate } from 'react-router-dom';
import { MealProvider } from './context/MealContext';
import Layout from './components/Layout';
import Planner from './pages/Planner';
import Recipes from './pages/Recipes';
import RecipeDetail from './pages/RecipeDetail';

const App: React.FC = () => {
  console.log("App: Rendering");
  return (
    <MealProvider>
      <HashRouter>
        <Routes>
          <Route path="/" element={<Layout />}>
            <Route index element={<Planner />} />
            <Route path="recipes" element={<Recipes />} />
            <Route path="recipes/:id" element={<RecipeDetail />} />
            <Route path="*" element={<Navigate to="/" replace />} />
          </Route>
        </Routes>
      </HashRouter>
    </MealProvider>
  );
};

export default App;
