import { useState } from 'react';
import { useDebounce } from '@/hooks/useDebounce';
import { useEventSearch } from '../queries';
import SearchResults from './SearchResults';

export default function SearchBar() {
    const [search, setSearch] = useState('');
    const searchResult = useDebounce(search.trim(),100);

    const { data: events = [], isError, isLoading } = useEventSearch(searchResult, search.length > 0);

    return (
        <div className="w-[30vw] relative">
            <input 
                type="search"
                placeholder="Search events"
                className={`p-4 ${search.trim() ? "rounded-t-3xl" : "rounded-3xl"} bg-white w-full outline-none`}
                value={search}
                onChange={(event) => setSearch(event.target.value)}
            />
            {search.trim() && (
                <SearchResults 
                    events = {events}
                    isLoading = {isLoading}
                    isError = {isError}
                />
            )}
        </div>
    )
}