import SearchBar from "@/features/events/components/SearchBar"

export default function HeroSection() {
    return (
        <div className="font-apple min-h-[40dvh] flex w-full items-center relative bg-hero-background">
            <div className="pointer-events-none" />
                <header className="relative flex min-h-[40dvh] flex-col justify-center gap-4 px-8 py-10">
                    <h1 className="text-4xl font-medium text-white">
                        Find your next experience.
                    </h1>
                    <SearchBar />
                </header>
            </div>
    )
}
