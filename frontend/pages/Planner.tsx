import React, { useState, useMemo } from 'react';
import { useMealContext } from '../context/MealContext';
import { Plus, Minus, Trash2, Calendar, ListTodo, X, ArrowRight, GripVertical, User, Users } from 'lucide-react';
import { Recipe, InventoryItem } from '../types';
import { Link } from 'react-router-dom';
import { BigCalendar } from '../components/BigCalendar';

const DAILY_TARGETS = {
  calories: 2000,
  protein: 60,
  carbs: 275,
  fat: 78
};

const Planner: React.FC = () => {
  const {
    plan,
    settings,
    updateSettings,
    removeMealFromDay,
    addMealToDay,
    updateMealPortions,
    recipes,
    inventory,
    toggleInventory,
    updateInventoryPortions,
    consumeInventoryPortions,
    removeFromInventory,
    t,
    language
  } = useMealContext();

  const [isModalOpen, setIsModalOpen] = useState(false);
  const [selectedDate, setSelectedDate] = useState<string | null>(null);
  const [isCalendarExpanded, setIsCalendarExpanded] = useState(() => {
    try {
      const saved = sessionStorage.getItem('isCalendarExpanded');
      // Default to true if not set or if set to anything other than 'false'
      return saved === 'false' ? false : true;
    } catch {
      return true;
    }
  });

  React.useEffect(() => {
    sessionStorage.setItem('isCalendarExpanded', String(isCalendarExpanded));
  }, [isCalendarExpanded]);
  const [showPercentages, setShowPercentages] = useState(false);

  // State for Side List (Meals To Do)
  const [isFridgeOpen, setIsFridgeOpen] = useState(false);
  const [planningFridgeItem, setPlanningFridgeItem] = useState<{ recipe: Recipe, portions: number, uid: string } | null>(null);

  // Portion Mode for Sidebar
  const [portionMode, setPortionMode] = useState<'myself' | 'custom'>('myself');
  const [customPortionCount, setCustomPortionCount] = useState(2);

  // Drag and Drop State
  const [dragOverDate, setDragOverDate] = useState<string | null>(null);

  const dateRange = useMemo(() => {
    const dates = [];
    let start = new Date(settings.startDate || new Date());
    if (isNaN(start.getTime())) start = new Date();

    for (let i = 0; i < settings.daysDuration; i++) {
      const d = new Date(start);
      d.setDate(d.getDate() + i);
      const offset = d.getTimezoneOffset();
      const localDate = new Date(d.getTime() - (offset * 60 * 1000));
      dates.push(localDate.toISOString().split('T')[0]);
    }
    return dates;
  }, [settings.startDate, settings.daysDuration]);

  // Map inventory items to full objects with recipe data
  const inventoryItems = useMemo(() => {
    return inventory.map(item => {
      const recipe = recipes.find(r => r.id === item.recipeId);
      return recipe ? { ...item, recipe } : null;
    }).filter(item => item !== null) as ({ recipe: Recipe } & InventoryItem)[];
  }, [recipes, inventory]);

  const handleOpenAddModal = (date: string | null) => {
    setSelectedDate(date);
    setIsModalOpen(true);
  };

  const handleSelectRecipe = (recipe: Recipe) => {
    if (selectedDate) {
      addMealToDay(selectedDate, recipe);
    } else {
      // Adding to Queue (Meals To Do)
      toggleInventory(recipe.id);
    }
    setIsModalOpen(false);
    setSelectedDate(null);
  };

  const handlePlanFridgeItem = (date: string) => {
    if (planningFridgeItem) {
      // Use the picker value for transfer amount
      const amountToTransfer = portionMode === 'myself' ? 1 : customPortionCount;
      addMealToDay(date, planningFridgeItem.recipe, amountToTransfer);
      consumeInventoryPortions(planningFridgeItem.uid, amountToTransfer);
      setPlanningFridgeItem(null);
    }
  };

  const handlePortionModeChange = (mode: 'myself' | 'custom') => {
    setPortionMode(mode);
  };

  const handleCustomPortionChange = (newCount: number) => {
    const validCount = Math.max(2, newCount);
    setCustomPortionCount(validCount);
  };

  // Drag and Drop Handlers
  const handleDragStart = (e: React.DragEvent, item: { recipe: Recipe, portions: number, uid: string }) => {
    // Determine how many to move based on global picker settings, not the item stock
    const amountToMove = portionMode === 'myself' ? 1 : customPortionCount;

    const data = {
      ...item.recipe,
      portions: amountToMove,
      fromInventoryUid: item.uid
    };
    e.dataTransfer.setData('application/json', JSON.stringify(data));
    e.dataTransfer.effectAllowed = 'move';
  };

  const handleDragOver = (e: React.DragEvent, date: string) => {
    e.preventDefault();
    setDragOverDate(date);
    e.dataTransfer.dropEffect = 'move';
  };

  const handleDragLeave = (e: React.DragEvent) => {
    // Prevent flickering when dragging over children by checking relation
    if (e.currentTarget.contains(e.relatedTarget as Node)) return;
    setDragOverDate(null);
  };

  const handleDrop = (e: React.DragEvent, date: string) => {
    e.preventDefault();
    setDragOverDate(null);
    try {
      const data = e.dataTransfer.getData('application/json');
      if (data) {
        const droppedItem = JSON.parse(data);

        // Add to the day using the portions carried over from drag source (which is the picker amount)
        addMealToDay(date, droppedItem, droppedItem.portions);

        // Consume that amount from inventory stock
        if (droppedItem.fromInventoryUid) {
          consumeInventoryPortions(droppedItem.fromInventoryUid, droppedItem.portions);
        }
      }
    } catch (err) {
      console.error("Failed to parse dropped data", err);
    }
  };

  const formatDateParts = (dateStr: string) => {
    const date = new Date(dateStr + 'T12:00:00');
    const locale = language === 'sk' ? 'sk-SK' : 'en-US';
    const dayName = new Intl.DateTimeFormat(locale, { weekday: 'short' }).format(date);
    const dayNum = new Intl.DateTimeFormat(locale, { day: 'numeric' }).format(date);
    const month = new Intl.DateTimeFormat(locale, { month: 'long' }).format(date);
    return { dayName, dayNum, month };
  };

  return (
    <div className="flex gap-6 relative">
      {/* Main Content Area */}
      <div className={`flex-1 space-y-8 pb-10 transition-all duration-300 ${isFridgeOpen ? 'mr-0 lg:mr-80' : ''}`}>

        {/* Top Section */}
        <div className="bg-white p-8 rounded-3xl shadow-lg shadow-gray-100/50 border border-white flex flex-col gap-6">
          {!isCalendarExpanded ? (
            <div className="flex justify-between items-center">
              <div>
                <h1 className="text-3xl font-extrabold text-gray-900 tracking-tight">{t('yourPlan')}</h1>
                <p className="text-gray-500 font-medium mt-1">
                  {t('starting')} {new Date(settings.startDate).toLocaleDateString(language === 'sk' ? 'sk-SK' : 'en-US')}
                </p>
              </div>
              <div className="flex items-center gap-3">
                <button
                  onClick={() => setIsFridgeOpen(!isFridgeOpen)}
                  className={`flex items-center px-5 py-3 rounded-2xl transition-all font-semibold text-sm border ${isFridgeOpen ? 'bg-blue-50 text-blue-600 border-blue-200' : 'bg-white text-gray-600 border-gray-200 hover:bg-gray-50'}`}
                >
                  <ListTodo className="w-4 h-4 mr-2" />
                  {t('mealsToDo')}
                  {inventory.length > 0 && (
                    <span className="ml-2 bg-blue-500 text-white text-[10px] px-2 py-0.5 rounded-full">{inventory.length}</span>
                  )}
                </button>
                <button
                  onClick={() => setIsCalendarExpanded(true)}
                  className="flex items-center px-5 py-3 bg-gray-900 text-white rounded-2xl hover:bg-gray-800 transition-all font-semibold text-sm shadow-xl shadow-gray-900/20"
                >
                  <Calendar className="w-4 h-4 mr-2" />
                  {t('changeDate')}
                </button>
              </div>
            </div>
          ) : (
            <div>
              <div className="mb-6 flex flex-col sm:flex-row justify-between items-start sm:items-center border-b border-gray-100 pb-6 gap-4">
                <div>
                  <h1 className="text-2xl font-bold text-gray-900">{t('calendar')}</h1>
                  <p className="text-gray-500 text-sm font-medium">{t('selectStart')}</p>
                </div>

                <button
                  onClick={() => setIsFridgeOpen(!isFridgeOpen)}
                  className={`flex items-center px-4 py-2 rounded-xl transition-all font-semibold text-sm border ${isFridgeOpen ? 'bg-blue-50 text-blue-600 border-blue-200' : 'bg-white text-gray-600 border-gray-200 hover:bg-gray-50'}`}
                >
                  <ListTodo className="w-4 h-4 mr-2" />
                  {t('mealsToDo')}
                  {inventory.length > 0 && (
                    <span className="ml-2 bg-blue-500 text-white text-[10px] px-1.5 py-0.5 rounded-full">{inventory.length}</span>
                  )}
                </button>
              </div>
              <BigCalendar
                startDate={settings.startDate || new Date().toISOString().split('T')[0]}
                daysDuration={settings.daysDuration}
                onDateSelect={(date) => updateSettings({ startDate: date })}
                onDurationChange={(days) => updateSettings({ daysDuration: days })}
                onMinimize={() => setIsCalendarExpanded(false)}
              />
            </div>
          )}
        </div>

        {/* Cards Grid */}
        <div className={`grid grid-cols-1 md:grid-cols-2 ${isFridgeOpen ? 'xl:grid-cols-3' : 'lg:grid-cols-3 xl:grid-cols-4 2xl:grid-cols-5'} gap-6`}>
          {dateRange.map((date) => {
            const meals = plan[date] || [];

            // Calculate Totals based on Portions
            const totals = meals.reduce((acc, curr) => ({
              calories: acc.calories + (curr.calories * curr.portions),
              protein: acc.protein + (curr.protein * curr.portions),
              carbs: acc.carbs + (curr.carbs * curr.portions),
              fat: acc.fat + (curr.fat * curr.portions),
            }), { calories: 0, protein: 0, carbs: 0, fat: 0 });

            const { dayName, dayNum } = formatDateParts(date);
            const isToday = date === new Date().toISOString().split('T')[0];
            const isDragOver = dragOverDate === date;

            return (
              <div
                key={date}
                onDragOver={(e) => handleDragOver(e, date)}
                onDragLeave={handleDragLeave}
                onDrop={(e) => handleDrop(e, date)}
                className={`
                  flex flex-col h-full min-h-[360px] rounded-3xl p-5 transition-all duration-300
                  ${isDragOver ? 'bg-blue-50 ring-2 ring-blue-400 scale-[1.02] shadow-xl' : ''}
                  ${isToday && !isDragOver ? 'bg-white ring-2 ring-primary ring-offset-2 ring-offset-surface shadow-xl shadow-primary/10' : ''}
                  ${!isToday && !isDragOver ? 'bg-white shadow-sm hover:shadow-lg border border-gray-50' : ''}
                `}
              >

                {/* Card Header */}
                <div className="flex justify-between items-start mb-6 pointer-events-none">
                  <div className="flex flex-col">
                    <span className={`text-xs font-bold uppercase tracking-wider mb-1 ${isToday ? 'text-primary' : 'text-gray-400'}`}>
                      {dayName}
                    </span>
                    <span className="text-3xl font-extrabold text-gray-900">{dayNum}</span>
                  </div>
                </div>

                {/* Meals List */}
                <div className="flex-1 space-y-4 mb-4">
                  {meals.length === 0 ? (
                    <div className={`h-full flex flex-col items-center justify-center text-center py-8 ${isDragOver ? 'opacity-100' : 'opacity-40'}`}>
                      <div className={`w-12 h-12 rounded-full flex items-center justify-center mb-2 ${isDragOver ? 'bg-blue-100' : 'bg-gray-100'}`}>
                        <Plus className={`w-6 h-6 ${isDragOver ? 'text-blue-500' : 'text-gray-400'}`} />
                      </div>
                      <span className={`text-sm font-semibold ${isDragOver ? 'text-blue-600' : 'text-gray-400'}`}>
                        {isDragOver ? t('dragToPlan') : t('emptyDay')}
                      </span>
                    </div>
                  ) : (
                    meals.map((meal, idx) => (
                      <div key={`${meal.uid || idx}`} className="group relative">
                        <div className="flex gap-3 p-2 rounded-2xl hover:bg-gray-50 transition-colors">
                          <img src={meal.image} alt={meal.title[language]} className="w-14 h-14 rounded-xl object-cover shadow-sm self-center" />
                          <div className="flex-1 min-w-0 py-1 flex flex-col justify-between">
                            <Link to={`/recipes/${meal.id}`} className="text-sm font-bold text-gray-900 truncate block hover:text-primary transition-colors">
                              {meal.title[language]}
                            </Link>

                            <div className="flex items-center justify-between mt-1">
                              {/* Portion Control */}
                              <div className="flex items-center bg-white rounded-lg border border-gray-200 shadow-sm h-6">
                                <button
                                  onClick={() => updateMealPortions(date, meal.uid, -1)}
                                  className="px-1.5 h-full hover:bg-gray-50 rounded-l-lg text-gray-500 hover:text-red-500 flex items-center justify-center"
                                >
                                  <Minus className="w-3 h-3" />
                                </button>
                                <span className="text-[10px] font-bold px-1 min-w-[1.2rem] text-center">{meal.portions}</span>
                                <button
                                  onClick={() => updateMealPortions(date, meal.uid, 1)}
                                  className="px-1.5 h-full hover:bg-gray-50 rounded-r-lg text-gray-500 hover:text-green-500 flex items-center justify-center"
                                >
                                  <Plus className="w-3 h-3" />
                                </button>
                              </div>

                              {/* Trash Button */}
                              <button
                                onClick={() => removeMealFromDay(date, meal.uid)}
                                className="text-gray-300 hover:text-red-500 p-1.5 rounded-lg transition-colors hover:bg-red-50"
                              >
                                <Trash2 className="w-4 h-4" />
                              </button>
                            </div>
                          </div>
                        </div>
                      </div>
                    ))
                  )}
                  {/* Visual Drop Placeholder if dragging over */}
                  {isDragOver && meals.length > 0 && (
                    <div className="h-16 border-2 border-dashed border-blue-300 rounded-2xl bg-blue-50/50 flex items-center justify-center">
                      <span className="text-blue-500 text-xs font-bold uppercase">{t('dragToPlan')}</span>
                    </div>
                  )}
                </div>

                {/* Nutrient Summary (Footer) */}
                {meals.length > 0 && (
                  <button
                    onClick={() => setShowPercentages(!showPercentages)}
                    className="w-full bg-gray-50 hover:bg-gray-100 transition-colors rounded-2xl p-3 mb-4 grid grid-cols-4 gap-1 divide-x divide-gray-200/50 cursor-pointer select-none"
                    title={t('clickToToggle')}
                  >
                    <div className="text-center px-1">
                      <div className="text-[10px] font-bold text-gray-400 uppercase mb-0.5">{t('kcal')}</div>
                      <div className="text-sm font-extrabold text-gray-900">
                        {showPercentages
                          ? `${Math.round((totals.calories / DAILY_TARGETS.calories) * 100)}%`
                          : Math.round(totals.calories)
                        }
                      </div>
                    </div>
                    <div className="text-center px-1">
                      <div className="text-[10px] font-bold text-gray-400 uppercase mb-0.5">{t('prot')}</div>
                      <div className="text-sm font-extrabold text-emerald-600">
                        {showPercentages
                          ? `${Math.round((totals.protein / DAILY_TARGETS.protein) * 100)}%`
                          : `${Math.round(totals.protein)}${t('g')}`
                        }
                      </div>
                    </div>
                    <div className="text-center px-1">
                      <div className="text-[10px] font-bold text-gray-400 uppercase mb-0.5">{t('carb')}</div>
                      <div className="text-sm font-extrabold text-blue-600">
                        {showPercentages
                          ? `${Math.round((totals.carbs / DAILY_TARGETS.carbs) * 100)}%`
                          : `${Math.round(totals.carbs)}${t('g')}`
                        }
                      </div>
                    </div>
                    <div className="text-center px-1">
                      <div className="text-[10px] font-bold text-gray-400 uppercase mb-0.5">{t('fat')}</div>
                      <div className="text-sm font-extrabold text-orange-500">
                        {showPercentages
                          ? `${Math.round((totals.fat / DAILY_TARGETS.fat) * 100)}%`
                          : `${Math.round(totals.fat)}${t('g')}`
                        }
                      </div>
                    </div>
                  </button>
                )}

                {/* Add Button */}
                <button
                  onClick={() => handleOpenAddModal(date)}
                  className="w-full py-3 rounded-2xl bg-gray-50 text-gray-400 font-bold text-sm hover:bg-primary hover:text-white transition-all duration-200 flex items-center justify-center group"
                >
                  <Plus className="w-4 h-4 mr-2 group-hover:scale-110 transition-transform" />
                  {t('addItem')}
                </button>
              </div>
            );
          })}
        </div>
      </div>

      {/* Meals To Do Side Panel (Fixed/Overlay on small, Side on large) */}
      <div
        className={`
          fixed inset-y-0 right-0 z-40 w-80 bg-white shadow-2xl transform transition-transform duration-300 ease-in-out border-l border-gray-100
          ${isFridgeOpen ? 'translate-x-0' : 'translate-x-full'}
        `}
      >
        <div className="flex flex-col h-full">
          {/* Sidebar Header */}
          <div className="p-4 border-b border-gray-100 bg-white/50 backdrop-blur-sm sticky top-0 z-10">
            <div className="flex justify-between items-center mb-4">
              <div className="flex items-center text-blue-800">
                <ListTodo className="w-5 h-5 mr-2" />
                <h2 className="font-bold text-lg">{t('mealsToDo')}</h2>
              </div>
              <button
                onClick={() => setIsFridgeOpen(false)}
                className="p-1.5 hover:bg-blue-50 text-blue-800 rounded-full transition-colors"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            {/* Portion Picker */}
            <div className="bg-gray-50 p-1.5 rounded-xl flex gap-1 mb-2">
              <button
                onClick={() => handlePortionModeChange('myself')}
                className={`
                    flex-1 flex items-center justify-center py-2 rounded-lg text-xs font-bold transition-all duration-200
                    ${portionMode === 'myself'
                    ? 'bg-white text-blue-600 shadow-sm ring-1 ring-gray-100'
                    : 'text-gray-400 hover:text-gray-600 hover:bg-gray-100'
                  }
                 `}
              >
                <User className="w-3.5 h-3.5 mr-1.5" />
                {t('planForMyself')}
              </button>
              <button
                onClick={() => handlePortionModeChange('custom')}
                className={`
                    flex-1 flex items-center justify-center py-2 rounded-lg text-xs font-bold transition-all duration-200
                    ${portionMode === 'custom'
                    ? 'bg-white text-blue-600 shadow-sm ring-1 ring-gray-100'
                    : 'text-gray-400 hover:text-gray-600 hover:bg-gray-100'
                  }
                 `}
              >
                <Users className="w-3.5 h-3.5 mr-1.5" />
                {t('planForCustom')}
              </button>
            </div>

            {/* Custom Number Input */}
            {portionMode === 'custom' && (
              <div className="flex items-center justify-between bg-blue-50 p-3 rounded-xl animate-fade-in border border-blue-100">
                <span className="text-xs font-bold text-blue-800 uppercase tracking-wider">{t('numberOfPeople')}</span>
                <div className="flex items-center bg-white rounded-lg shadow-sm border border-blue-100 h-8">
                  <button
                    onClick={() => handleCustomPortionChange(customPortionCount - 1)}
                    className="w-8 h-full flex items-center justify-center text-blue-500 hover:bg-blue-50 rounded-l-lg transition-colors"
                  >
                    <Minus className="w-3.5 h-3.5" />
                  </button>
                  <span className="w-8 text-center text-sm font-bold text-gray-900">{customPortionCount}</span>
                  <button
                    onClick={() => handleCustomPortionChange(customPortionCount + 1)}
                    className="w-8 h-full flex items-center justify-center text-blue-500 hover:bg-blue-50 rounded-r-lg transition-colors"
                  >
                    <Plus className="w-3.5 h-3.5" />
                  </button>
                </div>
              </div>
            )}
          </div>

          <div className="flex-1 overflow-y-auto p-4 space-y-3">
            <button
              onClick={() => handleOpenAddModal(null)}
              className="w-full py-3 rounded-2xl border-2 border-dashed border-blue-200 text-blue-500 font-bold text-sm hover:bg-blue-50 transition-all flex items-center justify-center group mb-4"
            >
              <Plus className="w-4 h-4 mr-2 group-hover:scale-110 transition-transform" />
              {t('addToQueue')}
            </button>

            {inventoryItems.length === 0 ? (
              <div className="text-center py-10 text-gray-400">
                <ListTodo className="w-12 h-12 mx-auto mb-3 opacity-20" />
                <p className="text-sm font-medium">{t('fridgeEmpty')}</p>
              </div>
            ) : (
              inventoryItems.map(item => (
                <div
                  key={item.uid}
                  draggable
                  onDragStart={(e) => handleDragStart(e, item)}
                  className="bg-white border border-gray-100 rounded-2xl p-3 shadow-sm hover:shadow-md transition-all cursor-move group relative"
                >
                  <div className="absolute top-1/2 -translate-y-1/2 left-2 text-gray-300 opacity-0 group-hover:opacity-100">
                    <GripVertical className="w-4 h-4" />
                  </div>
                  <div className="flex gap-3 mb-3 pl-4">
                    <img src={item.recipe.image} className="w-12 h-12 rounded-lg object-cover pointer-events-none" alt="" />
                    <div className="flex-1 min-w-0">
                      <p className="text-sm font-bold text-gray-900 line-clamp-2">{item.recipe.title[language]}</p>
                      <div className="flex items-center justify-between mt-1">
                        <p className="text-xs text-gray-400">{item.recipe.calories} kcal</p>

                        {/* Sidebar Portion Control */}
                        <div className="flex items-center bg-gray-50 rounded-lg border border-gray-100 shadow-sm h-5">
                          <button
                            onClick={() => updateInventoryPortions(item.uid, -1)}
                            className="px-1.5 h-full hover:bg-gray-100 rounded-l-lg text-gray-500 hover:text-red-500 flex items-center justify-center"
                          >
                            <Minus className="w-2.5 h-2.5" />
                          </button>
                          <span className="text-[9px] font-bold px-1 min-w-[1rem] text-center">{item.portions}</span>
                          <button
                            onClick={() => updateInventoryPortions(item.uid, 1)}
                            className="px-1.5 h-full hover:bg-gray-100 rounded-r-lg text-gray-500 hover:text-green-500 flex items-center justify-center"
                          >
                            <Plus className="w-2.5 h-2.5" />
                          </button>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div className="flex gap-2 pl-4">
                    <button
                      onClick={() => setPlanningFridgeItem(item)}
                      className="flex-1 bg-blue-500 hover:bg-blue-600 text-white text-xs font-bold py-2 rounded-xl transition-colors flex items-center justify-center"
                    >
                      <Calendar className="w-3 h-3 mr-1.5" />
                      {t('planThis')}
                    </button>
                    <button
                      onClick={() => removeFromInventory(item.uid)}
                      className="p-2 text-gray-400 hover:text-red-500 hover:bg-red-50 rounded-xl transition-colors"
                      title={t('removeFromFridge')}
                    >
                      <Trash2 className="w-4 h-4" />
                    </button>
                  </div>
                </div>
              ))
            )}
          </div>
        </div>
      </div>

      {/* Backdrop for Fridge on Mobile */}
      {isFridgeOpen && (
        <div
          className="fixed inset-0 bg-black/20 z-30 lg:hidden backdrop-blur-sm"
          onClick={() => setIsFridgeOpen(false)}
        ></div>
      )}

      {/* Modal - Add Meal */}
      {isModalOpen && (
        <div className="fixed inset-0 bg-gray-900/40 backdrop-blur-sm z-50 flex items-center justify-center p-4">
          <div className="bg-white rounded-3xl shadow-2xl max-w-2xl w-full max-h-[85vh] flex flex-col overflow-hidden animate-scale-in">
            <div className="p-6 border-b border-gray-100 flex justify-between items-center bg-white z-10">
              <div>
                <h2 className="text-2xl font-extrabold text-gray-900">
                  {selectedDate ? t('addMeal') : t('addToQueue')}
                </h2>
                <p className="text-sm text-gray-500 font-medium">
                  {selectedDate
                    ? new Date(selectedDate).toLocaleDateString(language === 'sk' ? 'sk-SK' : 'en-US', { weekday: 'long', month: 'long', day: 'numeric' })
                    : t('mealsToDo')
                  }
                </p>
              </div>
              <button
                onClick={() => setIsModalOpen(false)}
                className="p-2 bg-gray-100 rounded-full text-gray-500 hover:bg-gray-200 transition-colors"
              >
                <Plus className="w-6 h-6 rotate-45" />
              </button>
            </div>

            <div className="flex-1 overflow-y-auto p-6 bg-gray-50">
              {/* If adding to specific day, show Fridge Items first */}
              {selectedDate && inventoryItems.length > 0 && (
                <div className="mb-6">
                  <h3 className="text-sm font-bold text-blue-600 uppercase tracking-wide mb-3 flex items-center">
                    <ListTodo className="w-4 h-4 mr-2" />
                    {t('mealsToDo')}
                  </h3>
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    {inventoryItems.map(item => (
                      <button
                        key={`fridge-${item.uid}`}
                        onClick={() => {
                          // Add to day from inventory item
                          // Use the sidebar picker amount
                          const amount = portionMode === 'myself' ? 1 : customPortionCount;
                          addMealToDay(selectedDate, item.recipe, amount);
                          consumeInventoryPortions(item.uid, amount);
                          setIsModalOpen(false);
                          setSelectedDate(null);
                        }}
                        className="flex items-center p-3 rounded-2xl bg-blue-50 border border-blue-100 hover:border-blue-300 shadow-sm transition-all text-left group"
                      >
                        <img src={item.recipe.image} alt="" className="w-16 h-16 rounded-xl object-cover shadow-sm group-hover:scale-105 transition-transform" />
                        <div className="ml-4 flex-1">
                          <p className="text-sm font-bold text-gray-900 line-clamp-1 group-hover:text-blue-600 transition-colors">{item.recipe.title[language]}</p>
                          <div className="flex items-center gap-2 mt-1">
                            <span className="text-[10px] font-bold text-white bg-blue-500 px-2 py-0.5 rounded-full inline-block">{t('inFridge')}</span>
                            <span className="text-[10px] text-blue-400 font-semibold">{item.portions} {t('portions')}</span>
                          </div>
                        </div>
                      </button>
                    ))}
                  </div>
                </div>
              )}

              <h3 className="text-sm font-bold text-gray-400 uppercase tracking-wide mb-3">{t('all')} {t('recipes')}</h3>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                {recipes.map(recipe => (
                  <button
                    key={recipe.id}
                    onClick={() => handleSelectRecipe(recipe)}
                    className="flex items-center p-3 rounded-2xl bg-white shadow-sm border border-transparent hover:border-primary/30 hover:shadow-md transition-all text-left group"
                  >
                    <img src={recipe.image} alt="" className="w-20 h-20 rounded-xl object-cover shadow-sm group-hover:scale-105 transition-transform" />
                    <div className="ml-4">
                      <p className="text-sm font-bold text-gray-900 line-clamp-1 group-hover:text-primary transition-colors">{recipe.title[language]}</p>
                      <div className="flex items-center gap-3 mt-1.5">
                        <span className="text-xs font-semibold px-2 py-0.5 bg-orange-50 text-orange-600 rounded-md">
                          {recipe.calories} {t('kcal')}
                        </span>
                        <span className="text-xs font-medium text-gray-400">
                          {recipe.defaultPortions} {t('portions').toLowerCase()}
                        </span>
                      </div>
                    </div>
                  </button>
                ))}
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Dialog for "Plan This" from Side List (Mobile Fallback or Quick Action) */}
      {planningFridgeItem && (
        <div className="fixed inset-0 bg-gray-900/40 backdrop-blur-sm z-50 flex items-center justify-center p-4">
          <div className="bg-white rounded-3xl shadow-2xl max-w-sm w-full animate-scale-in p-6">
            <h3 className="text-xl font-bold text-gray-900 mb-4">{t('selectDayFor')} <span className="text-primary">{planningFridgeItem.recipe.title[language]}</span></h3>
            <div className="space-y-2 max-h-60 overflow-y-auto pr-2">
              {dateRange.map(date => {
                const { dayName, dayNum } = formatDateParts(date);
                return (
                  <button
                    key={`plan-${date}`}
                    onClick={() => handlePlanFridgeItem(date)}
                    className="w-full flex items-center justify-between p-3 rounded-xl bg-gray-50 hover:bg-primary hover:text-white transition-colors group"
                  >
                    <span className="font-medium">{dayName}, {dayNum}</span>
                    <ArrowRight className="w-4 h-4 opacity-0 group-hover:opacity-100 transition-opacity" />
                  </button>
                )
              })}
            </div>
            <button
              onClick={() => setPlanningFridgeItem(null)}
              className="w-full mt-4 py-2 text-gray-500 font-bold text-sm hover:bg-gray-100 rounded-xl transition-colors"
            >
              {t('back')}
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default Planner;