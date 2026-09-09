import {
    useQuery
} from "@tanstack/react-query";
import LoadingState from '@pages/loading';
import ErrorState from '@pages/error';
import HeroCard from "@components/cards/heroCard";

async function fetchEvents() {
    const response = await fetch('/events');
    if (!response.ok) {
        throw new Error('error fetching events');
    }
    const events = await response.json();
    return JSON.stringify(events);
}

export default function HomePage() {
    const { data: events, isError, error ,isLoading } = useQuery({
        queryKey: ['events'],
        queryFn: fetchEvents
    })

    if (isLoading) return <LoadingState />
    if (isError) return <ErrorState />

    return (
        <div className="">
            <HeroCard />
        </div>
    );
}