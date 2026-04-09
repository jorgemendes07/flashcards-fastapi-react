export default function Banner(props) {

    return (
        <div className="border-b-2 border-gray-200 flex items-center place-content-between px-6 py-4">
            <h1 className="text-xl">Flashcards App</h1>
            <button 
                onClick={props.onOpenModal}
                className="bg-orange-300 text-sm px-3 py-1 rounded-lg cursor-pointer hover:bg-orange-400"
            >
                + Novo Deck
            </button>
        </div>
    )
}