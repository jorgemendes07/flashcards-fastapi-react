import { useEffect, useState } from 'react';
import api from './services/api';
import DeckList from './components/DeckList';
import Banner from './components/Banner';
import NewDeckModal from './components/NewDeckModal';

function App() {
  const [isModalOpen, setIsModalOpen] = useState(false);
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
  
  return (
    <div>
      <Banner onOpenModal={openModal} />
      <DeckList decks={decks}/>

      {isModalOpen && <NewDeckModal onClose={closeModal} onDeckCreated={addDeckToList} />}
    </div>
  );
}

export default App;