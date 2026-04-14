import { useEffect, useState } from 'react';
import api from './services/api';
import DeckList from './components/DeckList';
import Banner from './components/Banner';
import NewDeckModal from './components/NewDeckModal';
import EditDeckModal from './components/EditDeckModal';

function App() {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [deckBeingEdited, setDeckBeingEdited] = useState(null);
  const [decks, setDecks] = useState([]);

    useEffect(() => {
        const fetchDecks = async () => {
            const response = await api.get('/decks/user/1')

            setDecks(response.data)
        }
        fetchDecks()
    }, []);

  const openModal = () => {
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false)
  };

  const addDeckToList = (newDeck) => {
    setDecks([...decks, newDeck])
  };

  const removeDeckFromList = (id) => {
    setDecks(decks.filter(deck => deck.id !== id));
  }

  const updateDeckInList = (updatedDeck) => {
    setDecks(decks.map(deck => {
      return deck.id === updatedDeck.id ? updatedDeck : deck
    }));
    setDeckBeingEdited(null);
  }
  
  return (
    <div>
      <Banner onOpenModal={openModal} />
      <DeckList 
        decks={decks} 
        onDelete={removeDeckFromList}
        onEdit={setDeckBeingEdited}
      />

      {isModalOpen && <NewDeckModal onClose={closeModal} onDeckCreated={addDeckToList} />}

      {deckBeingEdited && <EditDeckModal deck={deckBeingEdited} onClose={() => setDeckBeingEdited(null)} onUpdate={updateDeckInList} />}
    </div>
  );
}

export default App;