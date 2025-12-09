import React from 'react';
import { NavLink, Outlet } from 'react-router-dom';
import { Utensils, CalendarDays, ChefHat, Globe, WifiOff } from 'lucide-react';
import { useMealContext } from '../context/MealContext';

const Layout: React.FC = () => {
  const { t, language, updateSettings, isTestMode, saveError } = useMealContext();

  const toggleLanguage = () => {
    updateSettings({ language: language === 'sk' ? 'en' : 'sk' });
  };

  return (
    <div className="min-h-screen flex flex-col bg-surface">
      {/* Testing Mode Banner */}
      {isTestMode && (
         <div className="bg-amber-100 border-b border-amber-200 text-amber-900 px-4 py-3 text-center text-sm font-bold shadow-sm relative z-50">
           ⚠️ Testing Mode: Backend not connected. Using static fallback data.
         </div>
      )}

      {/* Save Error Banner */}
      {saveError && (
         <div className="bg-red-100 border-b border-red-200 text-red-900 px-4 py-2 text-center text-xs font-bold shadow-sm relative z-50 flex justify-center items-center">
           <WifiOff className="w-3 h-3 mr-2" />
           {t('connectionError') || "Connection lost. Changes are saved locally."}
         </div>
      )}

      {/* Navigation */}
      <nav className="bg-white/80 backdrop-blur-md sticky top-0 z-30 border-b border-gray-100">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-20">
            <div className="flex items-center">
              <div className="bg-primary/10 p-2 rounded-xl mr-3">
                <Utensils className="h-6 w-6 text-primary" />
              </div>
              <span className="text-xl font-bold text-gray-900 tracking-tight">Jedálniček</span>
            </div>
            
            <div className="flex items-center space-x-2 sm:space-x-4">
              <NavLink 
                to="/"
                className={({ isActive }) => 
                  `flex items-center px-4 py-2 rounded-full text-sm font-bold transition-all duration-200 ${
                    isActive 
                      ? 'bg-primary text-white shadow-lg shadow-primary/30' 
                      : 'text-gray-500 hover:bg-gray-100 hover:text-gray-900'
                  }`
                }
              >
                <CalendarDays className="w-4 h-4 mr-2" />
                {t('planner')}
              </NavLink>
              <NavLink 
                to="/recipes"
                className={({ isActive }) => 
                  `flex items-center px-4 py-2 rounded-full text-sm font-bold transition-all duration-200 ${
                    isActive 
                      ? 'bg-primary text-white shadow-lg shadow-primary/30' 
                      : 'text-gray-500 hover:bg-gray-100 hover:text-gray-900'
                  }`
                }
              >
                <ChefHat className="w-4 h-4 mr-2" />
                {t('recipes')}
              </NavLink>
              
              <button
                onClick={toggleLanguage}
                className="flex items-center px-3 py-2 rounded-full text-sm font-bold text-gray-500 hover:bg-gray-100 hover:text-gray-900 transition-all border border-transparent hover:border-gray-200 ml-2"
                title={t('language')}
              >
                <Globe className="w-4 h-4 mr-1.5" />
                <span className="uppercase">{language}</span>
              </button>
            </div>
          </div>
        </div>
      </nav>

      {/* Main Content */}
      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <Outlet />
      </main>

      {/* Footer */}
      <footer className="mt-auto py-8">
        <div className="max-w-7xl mx-auto px-4 text-center">
          <p className="text-sm font-medium text-gray-400">
            &copy; {new Date().getFullYear()} Jedálniček. {t('footerText')}
          </p>
        </div>
      </footer>
    </div>
  );
};

export default Layout;