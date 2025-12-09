import React, { useMemo } from 'react';
import { useParams, Link, useNavigate } from 'react-router-dom';
import { useMealContext } from '../context/MealContext';
import { ArrowLeft, Clock, Flame, List, CheckCircle, Activity, Droplet, Wheat } from 'lucide-react';
import RecipeCard from '../components/RecipeCard';

const RecipeDetail: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const { recipes, t, language } = useMealContext();

  const recipe = useMemo(() => {
    return recipes.find(r => r.id === Number(id));
  }, [id, recipes]);

  const relatedRecipes = useMemo(() => {
    if (!recipe) return [];
    return recipes.filter(r => recipe.relatedRecipeIds.includes(r.id));
  }, [recipe, recipes]);

  if (!recipe) {
    return (
      <div className="text-center py-20">
        <h2 className="text-2xl font-bold text-gray-900">{t('notFound')}</h2>
        <button onClick={() => navigate('/recipes')} className="mt-4 text-primary hover:underline">
          {t('backToRecipes')}
        </button>
      </div>
    );
  }

  return (
    <div className="max-w-4xl mx-auto space-y-8 animate-fade-in pb-10">
      {/* Back Nav */}
      <button 
        onClick={() => navigate(-1)} 
        className="flex items-center text-gray-500 hover:text-primary transition-colors mb-4"
      >
        <ArrowLeft className="w-4 h-4 mr-2" />
        {t('back')}
      </button>

      {/* Hero Section */}
      <div className="bg-white rounded-2xl shadow-sm overflow-hidden border border-gray-100">
        <div className="relative h-64 sm:h-80 md:h-96 w-full">
          <img 
            src={recipe.image} 
            alt={recipe.title[language]} 
            className="w-full h-full object-cover"
          />
          <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent flex items-end">
            <div className="p-6 md:p-8 text-white w-full">
              <div className="flex gap-2 mb-3">
                {recipe.tags[language].map(tag => (
                  <span key={tag} className="px-3 py-1 text-xs font-bold bg-primary text-white rounded-full border border-primary/50">
                    {tag}
                  </span>
                ))}
              </div>
              <h1 className="text-3xl md:text-5xl font-bold mb-4 tracking-tight">{recipe.title[language]}</h1>
              <div className="flex flex-wrap items-center gap-6 text-sm font-semibold text-gray-200">
                <div className="flex items-center bg-white/10 backdrop-blur-md px-3 py-1.5 rounded-lg">
                  <Clock className="w-4 h-4 mr-2" />
                  {recipe.prepTime} {t('min')}
                </div>
                <div className="flex items-center bg-white/10 backdrop-blur-md px-3 py-1.5 rounded-lg">
                  <Flame className="w-4 h-4 mr-2" />
                  {recipe.calories} {t('calories')}
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Nutrition Bar */}
        <div className="grid grid-cols-4 divide-x divide-gray-100 border-b border-gray-100">
            <div className="p-4 text-center">
                <div className="text-xs font-bold text-gray-400 uppercase tracking-wider mb-1">{t('protein')}</div>
                <div className="text-xl font-extrabold text-emerald-600">{recipe.protein}{t('g')}</div>
            </div>
            <div className="p-4 text-center">
                <div className="text-xs font-bold text-gray-400 uppercase tracking-wider mb-1">{t('carbs')}</div>
                <div className="text-xl font-extrabold text-blue-600">{recipe.carbs}{t('g')}</div>
            </div>
            <div className="p-4 text-center">
                <div className="text-xs font-bold text-gray-400 uppercase tracking-wider mb-1">{t('fat')}</div>
                <div className="text-xl font-extrabold text-orange-500">{recipe.fat}{t('g')}</div>
            </div>
            <div className="p-4 text-center bg-gray-50/50">
                <div className="text-xs font-bold text-gray-400 uppercase tracking-wider mb-1">{t('total')}</div>
                <div className="text-xl font-extrabold text-gray-800">{recipe.calories}</div>
            </div>
        </div>

        {/* Content Split */}
        <div className="grid md:grid-cols-3 gap-8 p-6 md:p-8">
          
          {/* Ingredients */}
          <div className="md:col-span-1 space-y-4">
            <h3 className="text-lg font-bold text-gray-900 flex items-center">
              <List className="w-5 h-5 mr-2 text-primary" />
              {t('ingredients')}
            </h3>
            <ul className="space-y-3 bg-gray-50 p-5 rounded-xl border border-gray-100">
              {recipe.ingredients[language].map((ing, idx) => (
                <li key={idx} className="flex items-start text-sm text-gray-700 font-medium leading-relaxed">
                  <span className="w-1.5 h-1.5 bg-primary rounded-full mt-2 mr-3 flex-shrink-0"></span>
                  {ing}
                </li>
              ))}
            </ul>
          </div>

          {/* Instructions */}
          <div className="md:col-span-2 space-y-4">
            <h3 className="text-lg font-bold text-gray-900 flex items-center">
              <CheckCircle className="w-5 h-5 mr-2 text-primary" />
              {t('instructions')}
            </h3>
            <div className="space-y-6">
              {recipe.instructions[language].map((step, idx) => (
                <div key={idx} className="flex gap-4 group">
                  <div className="flex-shrink-0 w-8 h-8 rounded-full bg-emerald-50 text-primary font-bold flex items-center justify-center text-sm border border-emerald-100 group-hover:bg-primary group-hover:text-white transition-colors">
                    {idx + 1}
                  </div>
                  <p className="text-gray-600 text-base leading-relaxed mt-1">
                    {step}
                  </p>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>

      {/* Related Recipes */}
      {relatedRecipes.length > 0 && (
        <div className="pt-8 border-t border-gray-200">
          <h2 className="text-2xl font-bold text-gray-900 mb-6">{t('youMightLike')}</h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            {relatedRecipes.map(related => (
              <RecipeCard key={related.id} recipe={related} compact />
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default RecipeDetail;
