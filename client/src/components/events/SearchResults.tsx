import type { Event } from "@/types/event.ts";
import type { ReactNode } from 'react';

interface SearchResultsProps {
    events: Event[],
    isLoading: boolean
    isError: boolean
}

type SearchStatus = 
    'LOADING' |
    'ERROR' |
    'EMPTY' |
    'SUCCESS'

const content: Record<SearchStatus, ReactNode> = {
    LOADING: (
        <div className="flex min-h-12 items-center">
            <div className="w-full h-8 overflow-hidden rounded-lg bg-search-loading-bar">
            </div>
        </div>
    ),
    ERROR: (
        <div className="font-normal">
            Please try again later
        </div>
    ),
    EMPTY: (
        <div className="font-normal">
            No results
        </div>
    ),
    SUCCESS: (
        {events.map((event)=>(
            <li key={event.id}>
                {event.name}
            </li>
        ))}
    )
}

export default function SearchResults({
    events,
    isLoading,
    isError
}: SearchResultsProps) {
    let status: SearchStatus = 'SUCCESS';

    if (isLoading) status = 'LOADING';
    else if (isError) status = 'ERROR';
    else if (events.length == 0) status = 'EMPTY';
    return (
        <div className="bg-white absolute p-4 inset-x-0 top-full rounded-b-3xl shadow-lg z-1 justify-center">
            {content[status]}
        </div>
    )
}
