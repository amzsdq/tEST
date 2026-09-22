import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import RunNowButton from '../components/RunNowButton';
import * as api from '../api/schedule';

jest.mock('../api/schedule');

describe('RunNowButton', () => {
  const scheduleId = 'demo-schedule-id';

  beforeEach(() => {
    jest.clearAllMocks();
  });

  test('renders idle state', () => {
    render(<RunNowButton scheduleId={scheduleId} />);
    expect(screen.getByRole('button', { name: /run now/i })).toBeInTheDocument();
  });

  test('calls triggerRunNow on click and shows success', async () => {
    api.triggerRunNow.mockResolvedValueOnce();

    render(<RunNowButton scheduleId={scheduleId} />);
    const btn = screen.getByRole('button', { name: /run now/i });
    fireEvent.click(btn);

    // pending state
    expect(btn).toBeDisabled();
    expect(screen.getByText(/triggering/i)).toBeInTheDocument();

    // wait for success state
    await waitFor(() => expect(screen.getByText(/triggered/i)).toBeInTheDocument());
    expect(api.triggerRunNow).toHaveBeenCalledWith(scheduleId);
  });

  test('shows error state when API fails', async () => {
    api.triggerRunNow.mockRejectedValueOnce(new Error('boom'));

    render(<RunNowButton scheduleId={scheduleId} />);
    fireEvent.click(screen.getByRole('button', { name: /run now/i }));

    await waitFor(() => expect(screen.getByText(/failed/i)).toBeInTheDocument());
    expect(api.triggerRunNow).toHaveBeenCalledWith(scheduleId);
  });
});
