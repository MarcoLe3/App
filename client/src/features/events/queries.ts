import { useQuery } from '@tanstack/react-query';
import { fetchEvents, searchEvents } from './api';

export function useEvents(offset: number, limit = 10) {
  return useQuery({
    queryKey: ['events', 'list', { offset, limit }],
    queryFn: () => fetchEvents(offset, limit),
  });
}

export function useEventSearch(search: string, enabled = search.length > 0, limit = 10) {
  return useQuery({
    queryKey: ['events', 'search', { search, limit }],
    queryFn: () => searchEvents(search, limit),
    enabled,
  });
}
