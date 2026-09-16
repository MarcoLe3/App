import type { Event } from '@/types/event.ts';

export async function fetchEvents(offset: number, limit: number): Promise<Event[]> {
  const response = await fetch(`/api/events?limit=${limit}&offset=${offset}`);
  if (!response.ok) throw new Error('error fetching events');
  const data = await response.json();
  return data.events;
}

export async function searchEvents(search: string, limit: number): Promise<Event[]> {
  const params = new URLSearchParams({ query: search, limit: String(limit) });
  const response = await fetch(`/api/events/search?${params}`);
  if (!response.ok) throw new Error('error searching for events');
  const data = await response.json();
  return data.events;
}

export async function login(username: string, password: string) {
    const response = await fetch(`/api/auth/token`, {
        method: 'POST',
        credentials: 'same-origin',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({username, password})
    });

    if (!response.ok) throw new Error('not valid');
    return response.json();
}