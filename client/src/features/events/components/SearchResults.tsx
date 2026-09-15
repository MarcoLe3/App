import type {Event} from "../types";

interface SearchResultsProps {
    events: Event[],
    isLoading: boolean
    isError: boolean
}

export default function SearchResults({
    events,
    isLoading,
    isError
}: SearchResultsProps) {
    return (
        <div className="bg-white absolute p-4 inset-x-0 top-full rounded-b-3xl shadow-lg z-1 justify-center">
            {isLoading ? (
                <div className="flex min-h-12 items-center">
                    <div className="w-full h-8 overflow-hidden rounded-lg bg-search-loading-bar">
                    </div>
                </div>
            ) : isError ? (
                <div className="font-normal">
                    Please try again later
                </div>
            ) : events.length === 0 ? (
                <div className="font-normal">
                    No results
                </div>
            ) : (
                <ul>
                    {events.map((event)=>(
                        <li key={event.id}>
                            {event.name}

                        </li>
                    ))}
                </ul>
            )}
        </div>
    )
}
