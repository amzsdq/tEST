import React, { useEffect, useState } from 'react';
import RunNowButton from './components/RunNowButton';
import ScheduleCard from './components/ScheduleCard';
import { fetchSchedule } from './api/schedule';

export default function App() {
  const [schedule, setSchedule] = useState(null);
  const [loading, setLoading] = useState(true);

  // Load a single schedule for demo purposes.
  useEffect(() => {
    async function load() {
      try {
        const data = await fetchSchedule('demo-schedule-id');
        setSchedule(data);
      } catch (e) {
        console.error('Failed to load schedule', e);
      } finally {
        setLoading(false);
      }
    }
    load();
  }, []);

  if (loading) {
    return (
      <div className="flex items-center justify-center h-screen">
        <span className="text-gray-600">Loading schedule…</span>
      </div>
    );
  }

  if (!schedule) {
    return (
      <div className="flex items-center justify-center h-screen">
        <span className="text-red-600">No schedule found.</span>
      </div>
    );
  }

  return (
    <div className="max-w-2xl mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Relay Research Scheduler</h1>
      <ScheduleCard schedule={schedule} />
      <div className="mt-6 flex gap-4">
        {/* Run‑now is deliberately separate from any schedule mutation */}
        <RunNowButton scheduleId={schedule.id} />
        {/* Placeholder for a future “Update Schedule” UI */}
        <button
          className="px-4 py-2 bg-indigo-600 text-white rounded hover:bg-indigo-700 transition"
          disabled
        >
          Update Schedule (WIP)
        </button>
      </div>
    </div>
  );
}
