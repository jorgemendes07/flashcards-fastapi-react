export default function Banner() {
    return (
        <div className="border-b-2 border-gray-200 flex items-center place-content-between px-6 py-4">
            <h1 className="text-3xl">Flashcards App</h1>
            <button className="bg-blue-300 p-2 rounded">+ Novo Deck</button>
        </div>
    )
}