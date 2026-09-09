import SearchBar from "@components/searchBar"

export default function HeroCard() {
    return (
        <div className="font-apple flex flex-col bg-hero-background">
            <h1 className="text-primary-text">Find your next experience.</h1>
            <SearchBar />
        </div>
    )
}