/**
 * Mock API layer.
 * In a real deployment these would hit a backend that separates
 * "run‑now" from schedule mutation.
 *
 * The functions return Promises to emulate async HTTP calls.
 */

const MOCK_SCHEDULE = {
  id: 'demo-schedule-id',
  rrule: 'FREQ=DAILY;INTERVAL=1;BYHOUR=9;BYMINUTE=30',
  nextOccurrence: new Date(Date.now() + 60 * 60 * 1000).toISOString(),
  lastRun: new Date(Date.now() - 24 * 60 * 60 * 1000).toISOString(),
};

/**
 * Fetch a schedule by ID.
 * @param {string} id
 * @returns {Promise<Object>}
 */
export async function fetchSchedule(id) {
  // Simulate network latency
  await new Promise((r) => setTimeout(r, 300));
  if (id !== MOCK_SCHEDULE.id) {
    throw new Error('Schedule not found');
  }
  return { ...MOCK_SCHEDULE };
}

/**
 * Trigger a "run‑now" for the given schedule.
 * This endpoint must NOT mutate the persisted schedule; it only
 * enqueues an immediate execution.
 *
 * @param {string} id
 * @returns {Promise<void>}
 */
export async function triggerRunNow(id) {
  await new Promise((r) => setTimeout(r, 500));
  if (id !== MOCK_SCHEDULE.id) {
    throw new Error('Invalid schedule ID');
  }
  // In a real implementation this would POST to /api/run-now
  console.info(`[Mock] Run‑now triggered for schedule ${id}`);
}
