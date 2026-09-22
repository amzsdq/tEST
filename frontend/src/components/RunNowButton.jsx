import React, { useState } from 'react';
import { triggerRunNow } from '../api/schedule';
import { CheckCircleIcon, XCircleIcon, ArrowPathIcon } from '@heroicons/react/24/outline';

export default function RunNowButton({ scheduleId }) {
  const [status, setStatus] = useState('idle'); // idle | pending | success | error

  const handleClick = async () => {
    setStatus('pending');
    try {
      await triggerRunNow(scheduleId);
      setStatus('success');
    } catch (e) {
      console.error(e);
      setStatus('error');
    } finally {
      // Reset to idle after a short delay so the UI can be reused
      setTimeout(() => setStatus('idle'), 2000);
    }
  };

  const getLabel = () => {
    switch (status) {
      case 'pending':
        return (
          <>
            <ArrowPathIcon className="w-5 h-5 animate-spin mr-2" />
            Triggering…
          </>
        );
      case 'success':
        return (
          <>
            <CheckCircleIcon className="w-5 h-5 text-green-500 mr-2" />
            Triggered
          </>
        );
      case 'error':
        return (
          <>
            <XCircleIcon className="w-5 h-5 text-red-500 mr-2" />
            Failed
          </>
        );
      default:
        return 'Run Now';
    }
  };

  return (
    <button
      onClick={handleClick}
      disabled={status === 'pending'}
      className={`flex items-center px-4 py-2 rounded transition ${
        status === 'error'
          ? 'bg-red-600 hover:bg-red-700 text-white'
          : status === 'success'
          ? 'bg-green-600 hover:bg-green-700 text-white'
          : 'bg-blue-600 hover:bg-blue-700 text-white'
      }`}
    >
      {getLabel()}
    </button>
  );
}
