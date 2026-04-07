import { useState, useEffect } from "react";
import api from "../../services/api";

export default function() {
    const [decks, setDecks] = useState([]);

    useEffect(() => {
        const fetchDecks = async () => {
            const response = await api.get('/decks/user/1')

            setDecks(response.data)
        }
        fetchDecks()
    }, [])

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