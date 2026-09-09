export default function EventCard({event}) {
    return (
        <div className="min-h-30 p-6">
            <h2>{event.name}</h2>
            <p>{event.description}</p>
        </div>
    )
}