import { useEffect, useState } from 'react';
import api from './services/api';
import DeckList from './components/DeckList';

function App() {
  
  return (
    <div>
      <DeckList />
    </div>
  );
}

export default App;