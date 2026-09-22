import React from 'react';
import { formatISO, parseISO } from 'date-fns';

export default function ScheduleCard({ schedule }) {
  const { id, rrule, nextOccurrence, lastRun } = schedule;

  const formatDate = (dateStr) => {
    if (!dateStr) return '—';
    try {
      return formatISO(parseISO(dateStr));
    } catch {
      return dateStr;
    }
  };

  return (
    <div className="border rounded-lg p-4 bg-white shadow-sm">
      <h2 className="text-lg font-medium mb-2">Schedule ID: {id}</h2>
      <dl className="grid grid-cols-2 gap-x-4 gap-y-2">
        <dt className="text-gray-600">RRULE</dt>
        <dd className="font-mono">{rrule}</dd>

        <dt className="text-gray-600">Next Occurrence</dt>
        <dd>{formatDate(nextOccurrence)}</dd>

        <dt className="text-gray-600">Last Run</dt>
        <dd>{formatDate(lastRun)}</dd>
      </dl>
    </div>
  );
}
