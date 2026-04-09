export default function({ decks }) {
    
    return (
        <div>
            <ul>
                {decks.map((deck) => (
                    <li key={deck.id}>{deck.name}</li>
                ))}
            </ul>
        </div>
    )
}