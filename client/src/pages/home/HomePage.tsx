import { useState } from 'react';
import LoadingState from '@/components/ui/LoadingState';
import ErrorState from '@/components/ui/ErrorState';
import HeroSection from './HeroSection';
import EventCard from '@/components/events/EventCard';
import { useEvents } from '@/features/events/queries';

export default function HomePage() {
    const [offset] = useState(0)
    const { data: events, isError, isPending } = useEvents(offset);

    if (isPending) return <LoadingState />
    if (isError) return <ErrorState />

    return (
        <div className="min-h-dvh w-full flex flex-col">
            <HeroSection />
            <h2></h2>
            <section className="min-h-[60dvh] p-6 flex justify-center">
                { 
                    events.length > 0
                        ? events.map(event => <EventCard key={event.id} event={event} />)
                        : <p className="text-2xl font-medium">No events currently.</p>
                }
            </section>
        </div>
    );
}