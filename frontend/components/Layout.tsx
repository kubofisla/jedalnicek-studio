import React from 'react';
import { NavLink, Outlet } from 'react-router-dom';
import { CalendarDays, ChefHat, Globe } from 'lucide-react';
import { useMealContext } from '../context/MealContext';

const Layout = () => {
    const { language, updateSettings } = useMealContext();

    const toggleLanguage = () => {
        const newLang = language === 'sk' ? 'en' : 'sk';
        updateSettings({ language: newLang });
    };

    return (
        <div className="min-h-screen flex flex-col bg-gray-50 text-gray-900 font-sans">
            <nav className="bg-white sticky top-0 z-30 border-b border-gray-200">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="flex justify-between h-16">
                        <div className="flex">
                            <div className="flex-shrink-0 flex items-center">
                                <span className="text-xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-violet-600 to-amber-600">
                                    Jedálniček
                                </span>
                            </div>
                            <div className="hidden sm:ml-6 sm:flex sm:space-x-8">
                                <NavLink to="/" className={({ isActive }) => isActive ? "border-violet-500 text-gray-900 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium" : "border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium"}>
                                    <CalendarDays className="w-4 h-4 mr-2" />
                                    Planner
                                </NavLink>
                                <NavLink to="/recipes" className={({ isActive }) => isActive ? "border-violet-500 text-gray-900 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium" : "border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium"}>
                                    <ChefHat className="w-4 h-4 mr-2" />
                                    Recipes
                                </NavLink>
                            </div>
                        </div>
                        <div className="flex items-center">
                            <button onClick={toggleLanguage} className="p-2 rounded-md text-gray-400 hover:text-gray-500 focus:outline-none flex items-center">
                                <Globe className="h-5 w-5" />
                                <span className="ml-2 uppercase text-sm font-bold">{language}</span>
                            </button>
                        </div>
                    </div>
                </div>
            </nav>

            <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8">
                <Outlet />
            </main>

            <footer className="bg-white border-t border-gray-200 mt-auto">
                <div className="max-w-7xl mx-auto py-6 px-4 overflow-hidden sm:px-6 lg:px-8">
                    <p className="text-center text-sm text-gray-500">
                        &copy; {new Date().getFullYear()} Jedálniček.
                    </p>
                </div>
            </footer>
        </div>
    );
};

export default Layout;
