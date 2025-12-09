import React, { useState, useMemo } from 'react';
import { X, Plus, Trash2, Save, Flame, Activity, Droplet, Wheat, Check } from 'lucide-react';
import { useMealContext } from '../context/MealContext';
import { Recipe } from '../types';

interface CreateRecipeModalProps {
  onClose: () => void;
}

interface IngredientRow {
  id: string;
  ingredientId?: string; // ID for backend relation
  name: string;
  quantity: string;
  unit: string;
}

const UNITS = ['g', 'ml', 'ks', 'lžička', 'lžíce', 'hrnek'];

export const CreateRecipeModal: React.FC<CreateRecipeModalProps> = ({ onClose }) => {
  const { t, availableIngredients, createRecipe, addIngredient, recipes, language } = useMealContext();
  
  // Form State
  const [title, setTitle] = useState('');
  const [prepTime, setPrepTime] = useState('30');
  const [portions, setPortions] = useState('2');
  
  const [ingredientRows, setIngredientRows] = useState<IngredientRow[]>([
    { id: '1', name: '', quantity: '', unit: 'g' }
  ]);
  
  const [instructions, setInstructions] = useState<string[]>(['']);
  
  const [tags, setTags] = useState<string[]>([]);
  const [tagInput, setTagInput] = useState('');
  
  // UI State
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [lastSavedRecipe, setLastSavedRecipe] = useState<Recipe | null>(null);
  
  // Autocomplete State
  const [activeIngredientRowId, setActiveIngredientRowId] = useState<string | null>(null);

  // New Ingredient Modal State
  const [isNewIngredientModalOpen, setIsNewIngredientModalOpen] = useState(false);
  const [newIngredientName, setNewIngredientName] = useState('');
  const [newIngredientNutrients, setNewIngredientNutrients] = useState({
    energy: '',
    protein: '',
    carbs: '',
    fat: '',
    fiber: '',
    sugar: ''
  });

  // --- Derived Data ---
  const allExistingTags = useMemo(() => {
    const tagsSet = new Set<string>();
    recipes.forEach(r => r.tags[language].forEach(tag => tagsSet.add(tag)));
    return Array.from(tagsSet);
  }, [recipes, language]);

  const tagSuggestions = useMemo(() => {
    if (!tagInput) return [];
    return allExistingTags.filter(tag => 
      tag.toLowerCase().includes(tagInput.toLowerCase()) && !tags.includes(tag)
    );
  }, [tagInput, allExistingTags, tags]);

  // --- Handlers ---

  const handleAddIngredient = () => {
    setIngredientRows(prev => [
      ...prev, 
      { id: Date.now().toString(), name: '', quantity: '', unit: 'g' }
    ]);
  };

  const handleRemoveIngredient = (id: string) => {
    setIngredientRows(prev => prev.filter(row => row.id !== id));
  };

  const handleIngredientChange = (id: string, field: keyof IngredientRow, value: any) => {
    setIngredientRows(prev => prev.map(row => 
      row.id === id ? { ...row, [field]: value } : row
    ));
  };

  const handleInstructionChange = (index: number, value: string) => {
    const newInstructions = [...instructions];
    newInstructions[index] = value;
    setInstructions(newInstructions);
  };

  const handleAddInstruction = () => {
    setInstructions([...instructions, '']);
  };

  const handleRemoveInstruction = (index: number) => {
    setInstructions(prev => prev.filter((_, i) => i !== index));
  };

  const handleTagInputKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      const trimmed = tagInput.trim();
      if (trimmed && !tags.includes(trimmed)) {
        setTags([...tags, trimmed]);
        setTagInput('');
      }
    }
  };

  const addTag = (tag: string) => {
    if (!tags.includes(tag)) {
        setTags([...tags, tag]);
        setTagInput('');
    }
  };

  const removeTag = (tag: string) => {
    setTags(tags.filter(t => t !== tag));
  };

  const handleOpenNewIngredientModal = (name: string) => {
    setNewIngredientName(name);
    setNewIngredientNutrients({ energy: '', protein: '', carbs: '', fat: '', fiber: '', sugar: '' });
    setIsNewIngredientModalOpen(true);
  };

  const handleSaveNewIngredient = async () => {
    if (!newIngredientName) return;

    // Create new ingredient object (context generates ID)
    const newIngredient = {
      name: newIngredientName,
      energy: parseFloat(newIngredientNutrients.energy) || 0,
      protein: parseFloat(newIngredientNutrients.protein) || 0,
      carbs: parseFloat(newIngredientNutrients.carbs) || 0,
      fat: parseFloat(newIngredientNutrients.fat) || 0,
      fiber: parseFloat(newIngredientNutrients.fiber) || 0,
      sugar: parseFloat(newIngredientNutrients.sugar) || 0,
    };

    const savedIngredient = await addIngredient(newIngredient);
    
    if (activeIngredientRowId) {
       handleIngredientChange(activeIngredientRowId, 'name', newIngredientName);
       // We can also set the ID here if we want strict linking immediately
       if (savedIngredient.id) {
          handleIngredientChange(activeIngredientRowId, 'ingredientId', savedIngredient.id);
       }
    }

    setIsNewIngredientModalOpen(false);
    setActiveIngredientRowId(null);
  };

  const handleSave = async () => {
    setIsSubmitting(true);
    
    // Prepare Data
    const validIngredients = ingredientRows
      .filter(row => row.name && row.quantity)
      .map(row => ({
        ingredientId: row.ingredientId, // Pass the ID
        name: row.name,
        quantity: parseFloat(row.quantity),
        unit: row.unit
      }));

    const validInstructions = instructions.filter(i => i.trim());

    const recipeData = {
      title,
      defaultPortions: parseInt(portions) || 1,
      ingredients: validIngredients,
      instructions: validInstructions,
      tags,
      prepTime: parseInt(prepTime) || 0
    };

    try {
      const savedRecipe = await createRecipe(recipeData);
      setLastSavedRecipe(savedRecipe);
    } catch (error) {
      console.error(error);
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="fixed inset-0 bg-gray-900/50 backdrop-blur-sm z-50 flex items-center justify-center p-4 overflow-y-auto">
      <div className="bg-white rounded-3xl shadow-2xl w-full max-w-3xl my-8 flex flex-col max-h-[90vh]">
        
        {/* Header */}
        <div className="p-6 border-b border-gray-100 flex justify-between items-center bg-white rounded-t-3xl sticky top-0 z-20">
          <div>
            <h2 className="text-2xl font-bold text-gray-900">{t('createRecipe') || "Create Recipe"}</h2>
            <p className="text-sm text-gray-500">{t('createRecipeSubtitle') || "Add a new meal to your collection"}</p>
          </div>
          <button onClick={onClose} className="p-2 hover:bg-gray-100 rounded-full text-gray-500 transition-colors">
            <X className="w-6 h-6" />
          </button>
        </div>

        <div className="flex-1 overflow-y-auto p-6 space-y-8">
          
          {/* Success Message & Nutrition Result */}
          {lastSavedRecipe && (
            <div className="bg-emerald-50 border border-emerald-100 rounded-2xl p-6 animate-fade-in mb-6">
              <div className="flex items-center gap-3 mb-4">
                <div className="w-8 h-8 rounded-full bg-emerald-500 text-white flex items-center justify-center">
                  <Check className="w-5 h-5" />
                </div>
                <div>
                  <h3 className="font-bold text-emerald-900">{t('recipeSaved') || "Recipe Saved Successfully!"}</h3>
                  <p className="text-sm text-emerald-700">{t('nutritionCalculated') || "Nutrition values calculated:"}</p>
                </div>
              </div>
              
              <div className="grid grid-cols-4 gap-2">
                 <div className="bg-white p-3 rounded-xl shadow-sm text-center">
                    <Flame className="w-4 h-4 text-orange-500 mx-auto mb-1" />
                    <div className="text-lg font-bold text-gray-900">{Math.round(lastSavedRecipe.calories)}</div>
                    <div className="text-xs text-gray-500 uppercase">{t('kcal')}</div>
                 </div>
                 <div className="bg-white p-3 rounded-xl shadow-sm text-center">
                    <Activity className="w-4 h-4 text-emerald-500 mx-auto mb-1" />
                    <div className="text-lg font-bold text-gray-900">{Math.round(lastSavedRecipe.protein)}g</div>
                    <div className="text-xs text-gray-500 uppercase">{t('protein')}</div>
                 </div>
                 <div className="bg-white p-3 rounded-xl shadow-sm text-center">
                    <Wheat className="w-4 h-4 text-blue-500 mx-auto mb-1" />
                    <div className="text-lg font-bold text-gray-900">{Math.round(lastSavedRecipe.carbs)}g</div>
                    <div className="text-xs text-gray-500 uppercase">{t('carbs')}</div>
                 </div>
                 <div className="bg-white p-3 rounded-xl shadow-sm text-center">
                    <Droplet className="w-4 h-4 text-yellow-500 mx-auto mb-1" />
                    <div className="text-lg font-bold text-gray-900">{Math.round(lastSavedRecipe.fat)}g</div>
                    <div className="text-xs text-gray-500 uppercase">{t('fat')}</div>
                 </div>
              </div>
            </div>
          )}

          {/* Basic Info */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="space-y-2">
              <label className="text-sm font-bold text-gray-700">{t('recipeTitle') || "Recipe Title"}</label>
              <input 
                type="text" 
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                className="w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition-all"
                placeholder={t('enterTitle') || "e.g., Avocado Toast"}
              />
            </div>
            <div className="grid grid-cols-2 gap-4">
              <div className="space-y-2">
                <label className="text-sm font-bold text-gray-700">{t('portions')}</label>
                <input 
                  type="number" 
                  value={portions}
                  onChange={(e) => setPortions(e.target.value)}
                  className="w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition-all"
                />
              </div>
              <div className="space-y-2">
                <label className="text-sm font-bold text-gray-700">{t('prepTime')} (min)</label>
                <input 
                  type="number" 
                  value={prepTime}
                  onChange={(e) => setPrepTime(e.target.value)}
                  className="w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition-all"
                />
              </div>
            </div>
          </div>

          {/* Ingredients Section */}
          <div>
            <div className="flex justify-between items-center mb-3">
              <label className="text-sm font-bold text-gray-700">{t('ingredients')}</label>
              <span className="text-xs text-gray-400 font-medium">Auto-suggest from backend</span>
            </div>
            <div className="space-y-3">
              {ingredientRows.map((row) => (
                <div key={row.id} className="flex gap-2 relative">
                  <div className="flex-1 relative">
                    <input 
                      type="text" 
                      value={row.name}
                      onFocus={() => setActiveIngredientRowId(row.id)}
                      // Clearing ID if user changes text manually to something else
                      onChange={(e) => {
                         handleIngredientChange(row.id, 'name', e.target.value);
                         handleIngredientChange(row.id, 'ingredientId', undefined);
                      }}
                      className="w-full px-4 py-2.5 rounded-xl border border-gray-200 focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none"
                      placeholder={t('ingredientName') || "Ingredient"}
                    />
                    
                    {/* Autocomplete Dropdown */}
                    {activeIngredientRowId === row.id && row.name.length > 1 && (
                      <div className="absolute top-full left-0 right-0 mt-1 bg-white border border-gray-100 rounded-xl shadow-xl z-30 max-h-40 overflow-y-auto">
                        {availableIngredients
                          .filter(i => i.name.toLowerCase().includes(row.name.toLowerCase()))
                          .map((suggestion) => (
                            <button
                              key={suggestion.id}
                              className="w-full text-left px-4 py-2 hover:bg-gray-50 text-sm font-medium text-gray-700"
                              onClick={() => {
                                handleIngredientChange(row.id, 'name', suggestion.name);
                                handleIngredientChange(row.id, 'ingredientId', suggestion.id);
                                setActiveIngredientRowId(null);
                              }}
                            >
                              {suggestion.name}
                            </button>
                          ))
                        }
                        {/* Option to create new ingredient if not found */}
                        {availableIngredients.filter(i => i.name.toLowerCase().includes(row.name.toLowerCase())).length === 0 && (
                           <button
                              onClick={() => handleOpenNewIngredientModal(row.name)}
                              className="w-full text-left px-4 py-2 hover:bg-blue-50 text-sm font-bold text-blue-600 flex items-center"
                           >
                              <Plus className="w-3 h-3 mr-2" />
                              {t('createTag') || "Create"} "{row.name}"
                           </button>
                        )}
                      </div>
                    )}
                    {/* Backdrop to close autocomplete */}
                    {activeIngredientRowId === row.id && (
                        <div className="fixed inset-0 z-20" onClick={() => setActiveIngredientRowId(null)}></div>
                    )}
                  </div>
                  
                  <input 
                    type="number" 
                    value={row.quantity}
                    onChange={(e) => handleIngredientChange(row.id, 'quantity', e.target.value)}
                    className="w-20 px-3 py-2.5 rounded-xl border border-gray-200 focus:border-primary outline-none"
                    placeholder="0"
                  />
                  
                  <select 
                    value={row.unit}
                    onChange={(e) => handleIngredientChange(row.id, 'unit', e.target.value)}
                    className="w-24 px-3 py-2.5 rounded-xl border border-gray-200 bg-gray-50 focus:border-primary outline-none"
                  >
                    {UNITS.map(u => <option key={u} value={u}>{u}</option>)}
                  </select>

                  <button 
                    onClick={() => handleRemoveIngredient(row.id)}
                    className="p-2 text-gray-400 hover:text-red-500 hover:bg-red-50 rounded-xl transition-colors"
                  >
                    <Trash2 className="w-5 h-5" />
                  </button>
                </div>
              ))}
              
              <button 
                onClick={handleAddIngredient}
                className="text-sm font-bold text-primary hover:text-primary/80 flex items-center mt-2"
              >
                <Plus className="w-4 h-4 mr-1" /> {t('addIngredient') || "Add Ingredient"}
              </button>
            </div>
          </div>

          {/* Instructions */}
          <div>
            <label className="text-sm font-bold text-gray-700 block mb-3">{t('instructions')}</label>
            <div className="space-y-3">
              {instructions.map((step, idx) => (
                <div key={idx} className="flex gap-3">
                  <div className="w-8 h-8 flex-shrink-0 bg-gray-100 rounded-full flex items-center justify-center text-sm font-bold text-gray-500 mt-1">
                    {idx + 1}
                  </div>
                  <textarea 
                    value={step}
                    onChange={(e) => handleInstructionChange(idx, e.target.value)}
                    rows={2}
                    className="flex-1 px-4 py-3 rounded-xl border border-gray-200 focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none resize-none"
                    placeholder={`${t('step') || "Step"} ${idx + 1}...`}
                  />
                  <button 
                    onClick={() => handleRemoveInstruction(idx)}
                    className="p-2 text-gray-400 hover:text-red-500 hover:bg-red-50 rounded-xl transition-colors h-fit mt-1"
                  >
                    <Trash2 className="w-5 h-5" />
                  </button>
                </div>
              ))}
              <button 
                onClick={handleAddInstruction}
                className="text-sm font-bold text-primary hover:text-primary/80 flex items-center ml-11"
              >
                <Plus className="w-4 h-4 mr-1" /> {t('addStep') || "Add Step"}
              </button>
            </div>
          </div>

          {/* Tags */}
          <div>
            <label className="text-sm font-bold text-gray-700 block mb-3">{t('tags') || "Tags"}</label>
            <div className="flex flex-wrap gap-2 mb-3">
              {tags.map(tag => (
                <span key={tag} className="px-3 py-1 bg-gray-100 text-gray-700 rounded-full text-sm font-medium flex items-center">
                  {tag}
                  <button onClick={() => removeTag(tag)} className="ml-2 hover:text-red-500">
                    <X className="w-3 h-3" />
                  </button>
                </span>
              ))}
            </div>
            <div className="relative">
              <input 
                type="text"
                value={tagInput}
                onChange={(e) => setTagInput(e.target.value)}
                onKeyDown={handleTagInputKeyDown}
                className="w-full px-4 py-2.5 rounded-xl border border-gray-200 focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none"
                placeholder={t('addTagPlaceholder') || "Type and press Enter to add tag..."}
              />
              {/* Autocomplete for Tags */}
              {tagInput && (
                <div className="absolute top-full left-0 right-0 mt-1 bg-white border border-gray-100 rounded-xl shadow-xl z-30 max-h-40 overflow-y-auto p-1">
                  {tagSuggestions.map(tag => (
                    <button
                      key={tag}
                      onClick={() => addTag(tag)}
                      className="w-full text-left px-4 py-2 hover:bg-gray-50 text-sm font-medium text-gray-700 rounded-lg"
                    >
                      {tag}
                    </button>
                  ))}
                  
                  {/* Create New Option */}
                  {!tagSuggestions.includes(tagInput) && !tags.includes(tagInput) && (
                    <button
                      onClick={() => addTag(tagInput)}
                      className="w-full text-left px-4 py-2 hover:bg-blue-50 text-sm font-bold text-blue-600 rounded-lg flex items-center"
                    >
                      <Plus className="w-4 h-4 mr-2" />
                      {t('createTag') || "Create"} "{tagInput}"
                    </button>
                  )}
                </div>
              )}
            </div>
          </div>

        </div>

        {/* Footer Actions */}
        <div className="p-6 border-t border-gray-100 bg-gray-50 rounded-b-3xl flex justify-end gap-3 sticky bottom-0 z-20">
          <button 
            onClick={onClose}
            className="px-6 py-3 rounded-xl font-bold text-gray-500 hover:bg-gray-200 transition-colors"
          >
            {t('close') || "Close"}
          </button>
          <button 
            onClick={handleSave}
            disabled={isSubmitting || !title || ingredientRows.length === 0}
            className={`
              px-8 py-3 rounded-xl font-bold text-white flex items-center transition-all shadow-lg shadow-primary/30
              ${isSubmitting ? 'bg-gray-400 cursor-not-allowed' : 'bg-primary hover:bg-primary/90'}
            `}
          >
            {isSubmitting ? (
              <span className="animate-pulse">{t('saving') || "Saving..."}</span>
            ) : (
              <>
                <Save className="w-5 h-5 mr-2" />
                {t('saveRecipe') || "Save Recipe"}
              </>
            )}
          </button>
        </div>
      </div>

      {/* --- Nested Modal for Creating New Ingredient --- */}
      {isNewIngredientModalOpen && (
        <div className="fixed inset-0 bg-black/40 backdrop-blur-sm z-[60] flex items-center justify-center p-4">
           <div className="bg-white rounded-2xl shadow-xl w-full max-w-sm overflow-hidden animate-scale-in">
              <div className="p-5 border-b border-gray-100 flex justify-between items-center bg-gray-50">
                 <h3 className="text-lg font-bold text-gray-900">{t('newIngredient') || "New Ingredient"}</h3>
                 <button onClick={() => setIsNewIngredientModalOpen(false)} className="p-1.5 hover:bg-gray-200 rounded-full text-gray-500">
                    <X className="w-5 h-5" />
                 </button>
              </div>
              <div className="p-6 space-y-4">
                 <div>
                    <label className="text-xs font-bold text-gray-500 uppercase tracking-wide mb-1 block">{t('ingredientName')}</label>
                    <input 
                       type="text" 
                       value={newIngredientName}
                       onChange={(e) => setNewIngredientName(e.target.value)}
                       className="w-full px-4 py-2 rounded-xl border border-gray-200 bg-gray-100 text-gray-700 font-medium focus:outline-none"
                       readOnly
                    />
                 </div>
                 
                 <p className="text-sm text-gray-500 italic">{t('enterNutrients') || "Enter nutrition values per 100g"}:</p>
                 
                 <div className="grid grid-cols-2 gap-4">
                    <div>
                       <label className="text-xs font-bold text-gray-500 uppercase tracking-wide mb-1 block">{t('kcal')}</label>
                       <input 
                          type="number"
                          value={newIngredientNutrients.energy}
                          onChange={(e) => setNewIngredientNutrients({...newIngredientNutrients, energy: e.target.value})} 
                          className="w-full px-3 py-2 rounded-xl border border-gray-200 focus:border-primary outline-none"
                          placeholder="0"
                       />
                    </div>
                    <div>
                       <label className="text-xs font-bold text-gray-500 uppercase tracking-wide mb-1 block">{t('protein')}</label>
                       <input 
                          type="number" 
                          value={newIngredientNutrients.protein}
                          onChange={(e) => setNewIngredientNutrients({...newIngredientNutrients, protein: e.target.value})} 
                          className="w-full px-3 py-2 rounded-xl border border-gray-200 focus:border-primary outline-none"
                          placeholder="0g"
                       />
                    </div>
                    <div>
                       <label className="text-xs font-bold text-gray-500 uppercase tracking-wide mb-1 block">{t('carbs')}</label>
                       <input 
                          type="number" 
                          value={newIngredientNutrients.carbs}
                          onChange={(e) => setNewIngredientNutrients({...newIngredientNutrients, carbs: e.target.value})} 
                          className="w-full px-3 py-2 rounded-xl border border-gray-200 focus:border-primary outline-none"
                          placeholder="0g"
                       />
                    </div>
                    <div>
                       <label className="text-xs font-bold text-gray-500 uppercase tracking-wide mb-1 block">{t('fat')}</label>
                       <input 
                          type="number" 
                          value={newIngredientNutrients.fat}
                          onChange={(e) => setNewIngredientNutrients({...newIngredientNutrients, fat: e.target.value})} 
                          className="w-full px-3 py-2 rounded-xl border border-gray-200 focus:border-primary outline-none"
                          placeholder="0g"
                       />
                    </div>
                     <div>
                       <label className="text-xs font-bold text-gray-500 uppercase tracking-wide mb-1 block">Fiber</label>
                       <input 
                          type="number" 
                          value={newIngredientNutrients.fiber}
                          onChange={(e) => setNewIngredientNutrients({...newIngredientNutrients, fiber: e.target.value})} 
                          className="w-full px-3 py-2 rounded-xl border border-gray-200 focus:border-primary outline-none"
                          placeholder="0g"
                       />
                    </div>
                    <div>
                       <label className="text-xs font-bold text-gray-500 uppercase tracking-wide mb-1 block">Sugar</label>
                       <input 
                          type="number" 
                          value={newIngredientNutrients.sugar}
                          onChange={(e) => setNewIngredientNutrients({...newIngredientNutrients, sugar: e.target.value})} 
                          className="w-full px-3 py-2 rounded-xl border border-gray-200 focus:border-primary outline-none"
                          placeholder="0g"
                       />
                    </div>
                 </div>

                 <button 
                    onClick={handleSaveNewIngredient}
                    className="w-full mt-4 py-3 rounded-xl bg-primary text-white font-bold hover:bg-primary/90 transition-all shadow-lg shadow-primary/20"
                 >
                    {t('createAndAdd') || "Create & Add"}
                 </button>
              </div>
           </div>
        </div>
      )}
    </div>
  );
};