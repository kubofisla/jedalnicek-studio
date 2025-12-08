import React, { useState, useEffect, useMemo } from 'react';
import { ChevronLeft, ChevronRight, Minimize2, Clock } from 'lucide-react';
import { useMealContext } from '../context/MealContext';

interface BigCalendarProps {
  startDate: string; // YYYY-MM-DD
  daysDuration: number;
  onDateSelect: (date: string) => void;
  onDurationChange: (days: number) => void;
  onMinimize: () => void;
}

export const BigCalendar: React.FC<BigCalendarProps> = ({
  startDate,
  daysDuration,
  onDateSelect,
  onDurationChange,
  onMinimize
}) => {
  const { t, language } = useMealContext();
  const safeStartDate = startDate || new Date().toISOString().split('T')[0];
  const [year, month, day] = safeStartDate.split('-').map(Number);
  const [viewDate, setViewDate] = useState(new Date(year, month - 1, 1));

  useEffect(() => {
    // Sync view when startDate changes significantly
    setViewDate(new Date(year, month - 1, 1));
  }, [startDate, year, month]);

  // Generate localized arrays
  const { daysOfWeek, monthName } = useMemo(() => {
    const locale = language === 'sk' ? 'sk-SK' : 'en-US';

    // Days of week
    const days = [];
    for (let i = 0; i < 7; i++) {
      // Create a date that is a Sunday (e.g., Jan 1 2023)
      const d = new Date(2023, 0, 1 + i);
      days.push(new Intl.DateTimeFormat(locale, { weekday: 'short' }).format(d));
    }

    // Current Month Name
    const mName = new Intl.DateTimeFormat(locale, { month: 'long', year: 'numeric' }).format(viewDate);

    // Capitalize first letter for consistency
    const capitalizedMonth = mName.charAt(0).toUpperCase() + mName.slice(1);

    return { daysOfWeek: days, monthName: capitalizedMonth };
  }, [language, viewDate]);

  const getDaysInMonth = (y: number, m: number) => new Date(y, m + 1, 0).getDate();
  const getFirstDayOfMonth = (y: number, m: number) => new Date(y, m, 1).getDay();

  const currentYear = viewDate.getFullYear();
  const currentMonth = viewDate.getMonth();

  const daysInMonth = getDaysInMonth(currentYear, currentMonth);
  const firstDay = getFirstDayOfMonth(currentYear, currentMonth);

  const handlePrevMonth = () => {
    setViewDate(new Date(currentYear, currentMonth - 1, 1));
  };

  const handleNextMonth = () => {
    setViewDate(new Date(currentYear, currentMonth + 1, 1));
  };

  const handleDateClick = (dayNum: number) => {
    const m = currentMonth + 1;
    const dateStr = `${currentYear}-${m.toString().padStart(2, '0')}-${dayNum.toString().padStart(2, '0')}`;
    onDateSelect(dateStr);
  };

  const isStartDate = (d: number) => {
    return currentYear === year && currentMonth === (month - 1) && d === day;
  };

  const isInRange = (d: number) => {
    const checkDate = new Date(currentYear, currentMonth, d);
    const start = new Date(year, month - 1, day);
    const end = new Date(year, month - 1, day + daysDuration - 1);
    checkDate.setHours(0, 0, 0, 0);
    start.setHours(0, 0, 0, 0);
    end.setHours(0, 0, 0, 0);
    return checkDate >= start && checkDate <= end;
  };

  const calendarGrid = [];

  for (let i = 0; i < firstDay; i++) {
    calendarGrid.push(<div key={`empty-${i}`} className="h-12 w-full"></div>);
  }

  for (let i = 1; i <= daysInMonth; i++) {
    const isStart = isStartDate(i);
    const inRange = isInRange(i);

    // Style logic for range visuals
    const checkDate = new Date(currentYear, currentMonth, i);
    const start = new Date(year, month - 1, day);
    const end = new Date(year, month - 1, day + daysDuration - 1);
    checkDate.setHours(0, 0, 0, 0);
    start.setHours(0, 0, 0, 0);
    end.setHours(0, 0, 0, 0);

    const isRangeStart = checkDate.getTime() === start.getTime();
    const isRangeEnd = checkDate.getTime() === end.getTime();

    let bgClass = 'hover:bg-gray-50 text-gray-700';
    if (inRange) bgClass = 'bg-emerald-50 text-emerald-700';
    if (isStart) bgClass = 'bg-primary text-white shadow-lg shadow-primary/30 z-10';

    // Rounded corners for range visualization
    let roundClass = 'rounded-2xl'; // Default independent
    if (inRange && !isStart) {
      if (isRangeStart) roundClass = 'rounded-l-2xl rounded-r-none';
      else if (isRangeEnd) roundClass = 'rounded-r-2xl rounded-l-none';
      else roundClass = 'rounded-none';
    }
    // If it's the start date (user selection), keep it fully rounded to pop out
    if (isStart) roundClass = 'rounded-2xl scale-110';

    calendarGrid.push(
      <button
        key={i}
        onClick={() => handleDateClick(i)}
        className={`
          relative h-12 w-full flex items-center justify-center text-sm font-bold transition-all duration-200
          ${bgClass} ${roundClass}
        `}
      >
        {i}
      </button>
    );
  }

  return (
    <div className="animate-fade-in px-2">
      {/* Header Controls */}
      <div className="flex flex-col sm:flex-row justify-between items-center mb-8 gap-6">
        <div className="flex items-center gap-4">
          <button onClick={handlePrevMonth} className="p-3 bg-gray-50 hover:bg-white hover:shadow-md rounded-2xl text-gray-600 transition-all">
            <ChevronLeft className="w-5 h-5" />
          </button>
          <span className="text-xl font-bold text-gray-900 w-40 text-center capitalize">
            {monthName}
          </span>
          <button onClick={handleNextMonth} className="p-3 bg-gray-50 hover:bg-white hover:shadow-md rounded-2xl text-gray-600 transition-all">
            <ChevronRight className="w-5 h-5" />
          </button>
        </div>

        <div className="flex items-center gap-3 bg-white p-1.5 rounded-2xl border border-gray-100 shadow-sm">
          <div className="flex items-center px-4 py-2 bg-gray-50 rounded-xl">
            <Clock className="w-4 h-4 text-primary mr-2" />
            <input
              type="number"
              min="1"
              max="14"
              value={daysDuration}
              onChange={(e) => onDurationChange(parseInt(e.target.value) || 1)}
              className="w-8 bg-transparent font-bold text-gray-900 focus:outline-none text-center"
            />
            <span className="text-xs font-semibold text-gray-500 uppercase tracking-wide ml-1">{t('days')}</span>
          </div>

          <button
            onClick={onMinimize}
            className="p-3 text-gray-400 hover:text-gray-900 hover:bg-gray-50 rounded-xl transition-colors"
            title="Minimize Calendar"
          >
            <Minimize2 className="w-5 h-5" />
          </button>
        </div>
      </div>

      {/* Calendar Grid */}
      <div className="mb-2">
        <div className="grid grid-cols-7 mb-4">
          {daysOfWeek.map(day => (
            <div key={day} className="text-center text-xs font-bold text-gray-400 uppercase tracking-widest">
              {day}
            </div>
          ))}
        </div>
        <div className="grid grid-cols-7 gap-y-2">
          {calendarGrid}
        </div>
      </div>
    </div>
  );
};
