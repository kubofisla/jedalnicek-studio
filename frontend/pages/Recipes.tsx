import React, { useState, useMemo } from 'react';
import { useMealContext } from '../context/MealContext';
import RecipeCard from '../components/RecipeCard';
import { Search, Filter, Plus } from 'lucide-react';
import { CreateRecipeModal } from '../components/CreateRecipeModal';

const Recipes: React.FC = () => {
  const { recipes, t, language } = useMealContext();
  const [activeFilter, setActiveFilter] = useState<string>('All');
  const [searchQuery, setSearchQuery] = useState('');
  const [isCreateModalOpen, setIsCreateModalOpen] = useState(false);

  // Extract unique tags in current language
  const allTags = useMemo(() => {
    const tags = new Set<string>([t('all')]);
    recipes.forEach(r => r.tags?.[language]?.forEach(tag => tags.add(tag)));
    return Array.from(tags).sort();
  }, [recipes, language, t]);

  // Handle filter reset when language changes
  React.useEffect(() => {
    setActiveFilter(t('all'));
  }, [language, t]);

  // Filter recipes 
  const filteredRecipes = useMemo(() => {
    return recipes.filter(recipe => {
      const matchesTag = activeFilter === t('all') || recipe.tags?.[language]?.includes(activeFilter);
      const matchesSearch = recipe.title?.[language]?.toLowerCase().includes(searchQuery.toLowerCase());
      return matchesTag && matchesSearch;
    });
  }, [recipes, activeFilter, searchQuery, language, t]);

  return (
    <div className="space-y-8">
      {/* Header & Controls */}
      <div className="space-y-6">
        <div className="flex justify-between items-start">
          <div>
            <h1 className="text-3xl font-bold text-gray-900">{t('recipeCollection')}</h1>
            <p className="text-gray-500 mt-2">{t('recipeSubtitle')}</p>
          </div>

          <button
            onClick={() => setIsCreateModalOpen(true)}
            className="flex items-center bg-primary hover:bg-emerald-600 text-white px-5 py-3 rounded-2xl font-bold transition-all shadow-lg shadow-primary/20"
          >
            <Plus className="w-5 h-5 mr-2" />
            {t('createRecipe') || "Create Recipe"}
          </button>
        </div>

        <div className="flex flex-col md:flex-row gap-4 justify-between items-start md:items-center">
          {/* Search */}
          <div className="relative w-full md:w-96">
            <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
              <Search className="h-5 w-5 text-gray-400" />
            </div>
            <input
              type="text"
              placeholder={t('searchRecipes')}
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="block w-full pl-10 pr-3 py-2 border border-gray-300 rounded-lg leading-5 bg-white placeholder-gray-500 focus:outline-none focus:ring-primary focus:border-primary sm:text-sm"
            />
          </div>

          {/* Tag Cloud */}
          <div className="flex flex-wrap gap-2">
            <Filter className="w-5 h-5 text-gray-400 mr-2 self-center" />
            {allTags.map(tag => (
              <button
                key={tag}
                onClick={() => setActiveFilter(tag)}
                className={`px-4 py-1.5 rounded-full text-sm font-medium transition-all ${activeFilter === tag
                  ? 'bg-primary text-white shadow-md'
                  : 'bg-white text-gray-600 border border-gray-200 hover:bg-gray-50'
                  }`}
              >
                {tag}
              </button>
            ))}
          </div>
        </div>
      </div>

      {/* Grid */}
      {filteredRecipes.length > 0 ? (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          {filteredRecipes.map(recipe => (
            <RecipeCard key={recipe.id} recipe={recipe} />
          ))}
        </div>
      ) : (
        <div className="text-center py-20 bg-white rounded-xl border border-dashed border-gray-300">
          <p className="text-gray-500 text-lg">{t('noRecipes')}</p>
          <button
            onClick={() => { setActiveFilter(t('all')); setSearchQuery(''); }}
            className="mt-4 text-primary font-medium hover:underline"
          >
            {t('clearFilters')}
          </button>
        </div>
      )}

      {/* Create Modal */}
      {isCreateModalOpen && (
        <CreateRecipeModal onClose={() => setIsCreateModalOpen(false)} />
      )}
    </div>
  );
};

export default Recipes;