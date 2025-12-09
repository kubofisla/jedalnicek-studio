import React from 'react';
import { Clock, Flame, ListTodo } from 'lucide-react';
import { Recipe } from '../types';
import { Link } from 'react-router-dom';
import { useMealContext } from '../context/MealContext';

interface RecipeCardProps {
  recipe: Recipe;
  compact?: boolean;
}

const RecipeCard: React.FC<RecipeCardProps> = ({ recipe, compact = false }) => {
  const { language, t, inventory, toggleInventory } = useMealContext();
  
  // Check if at least one instance of this recipe exists in inventory
  const isInFridge = inventory.some(item => item.recipeId === recipe.id);

  const handleToggleFridge = (e: React.MouseEvent) => {
    e.preventDefault(); // Prevent navigation
    e.stopPropagation();
    toggleInventory(recipe.id);
  };

  return (
    <Link 
      to={`/recipes/${recipe.id}`}
      className="group block bg-white rounded-3xl shadow-sm hover:shadow-xl hover:shadow-gray-200/50 transition-all duration-300 overflow-hidden border border-gray-100 relative"
    >
      <div className={`relative ${compact ? 'h-32' : 'h-56'} overflow-hidden`}>
        <img 
          src={recipe.image} 
          alt={recipe.title[language]} 
          className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
        />
        
        {/* Top Right Badges */}
        <div className="absolute top-3 right-3 flex flex-col items-end gap-2">
          {/* Tags */}
          {recipe.tags[language].slice(0, 2).map(tag => (
            <span key={tag} className="px-3 py-1 text-[10px] uppercase tracking-wider font-bold bg-white/95 text-gray-900 rounded-full shadow-sm backdrop-blur-md">
              {tag}
            </span>
          ))}
          
          {/* Fridge/ToDo Toggle */}
          <button
            onClick={handleToggleFridge}
            className={`
              flex items-center justify-center w-8 h-8 rounded-full shadow-sm backdrop-blur-md transition-all duration-200 z-10
              ${isInFridge 
                ? 'bg-blue-500 text-white' 
                : 'bg-white/90 text-gray-400 hover:text-blue-500 hover:bg-white'
              }
            `}
            title={isInFridge ? t('removeFromFridge') : t('addToFridge')}
          >
            <ListTodo className="w-4 h-4" />
          </button>
        </div>

        {/* In Fridge Indicator Overlay (if active) */}
        {isInFridge && (
           <div className="absolute bottom-2 left-2 px-2 py-1 bg-blue-500/90 backdrop-blur-sm rounded-lg flex items-center shadow-lg">
              <ListTodo className="w-3 h-3 text-white mr-1.5" />
              <span className="text-[10px] font-bold text-white uppercase tracking-wide">{t('inFridge')}</span>
           </div>
        )}
      </div>
      
      <div className="p-5">
        <h3 className={`font-bold text-gray-900 ${compact ? 'text-sm' : 'text-xl'} mb-3 line-clamp-1 group-hover:text-primary transition-colors`}>
          {recipe.title[language]}
        </h3>
        
        <div className="flex items-center space-x-4 text-gray-500">
          <div className="flex items-center text-xs font-semibold bg-gray-50 px-2 py-1 rounded-lg">
            <Clock className="w-3 h-3 mr-1.5 text-primary" />
            {recipe.prepTime} {t('min')}
          </div>
          <div className="flex items-center text-xs font-semibold bg-gray-50 px-2 py-1 rounded-lg">
            <Flame className="w-3 h-3 mr-1.5 text-orange-500" />
            {recipe.calories} {t('kcal')}
          </div>
        </div>
      </div>
    </Link>
  );
};

export default RecipeCard;