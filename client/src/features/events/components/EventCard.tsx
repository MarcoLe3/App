import type { Event } from "../types";

export default function EventCard({event}: { event: Event }) {
    return (
        <div className="min-h-30 p-6">
            <hgroup>
                <h2>{event.genre}</h2>
                <h2>{event.name}</h2>
            </hgroup>
        </div>
    )
}