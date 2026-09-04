import {
    useQuery
} from "@tanstack/react-query";
import LoadingState from '@components/states/loading';
import ErrorState from '@components/states/error';
import SearchBar from '@components/searchBar';

async function fetchEvents() {
    const response = await fetch('/events');
    if (!response.ok) {
        throw new Error('error fetching events');
    }

    return JSON.stringify(response)
}

export default function HomePage() {
    const { data: events, isError, error ,isLoading } = useQuery({
        queryKey: ['events'],
        queryFn: fetchEvents
    })

    return (
        <>
            <SearchBar />
            <div>
                {
                    isLoading ? <LoadingState/> : 
                    error ? <ErrorState/> : 
                    <p>{events}</p>
                }
            </div>
        </>
    );
}