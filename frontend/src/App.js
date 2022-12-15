import './App.css';
import React, { Suspense, lazy } from 'react';
import Recipes from './recipes';
import Plan from './plan';
import Navbar from './navbar';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';

function App() {
    return (
        <Router>
            <Navbar />
            <Routes>
                <Route path="/recipes" element={<Recipes />} />
                <Route path="/plan" element={<Plan />} />
            </Routes>
        </Router>
    );
}

export default App;
