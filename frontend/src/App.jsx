import { useEffect, useState } from 'react';
import api from './services/api';
import DeckList from './components/DeckList';
import Banner from './components/Banner';

function App() {
  
  return (
    <div>
      <Banner />
      <DeckList />
    </div>
  );
}

export default App;