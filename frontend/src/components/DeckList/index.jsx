import deckIcon from './../../assets/deck-icon.png'

export default function({ decks }) {
    
    return (
        <div className="bg-gray-100 h-screen p-4 m-auto">
            <div>
                <h2 className='text-xl'>Seus Decks</h2>
                <p className='text-sm'>Selecione um deck para começar a práticar</p>
            </div>
            <div>
                {decks.map((deck) => (
                    <div className="flex rounded-md h-18 w-[95%] h-18 m-auto mt-3 p-3 bg-white text-gray-600 cursor-pointer transition-all duration-300 hover:-translate-y-1 hover:shadow-md">
                        <img src={deckIcon} alt="Icone de cartas de baralho"
                            className='w-8 h-8 rounded-lg mr-4'
                        />
                        <div className='flex flex-1 justify-between'>
                            <div 
                                key={deck.id}
                            >
                                {deck.name}
                            </div>
                            <div className='text-sm text-gray-400'>
                                <i className="fa-solid fa-pen cursor-pointer mr-1 hover:text-gray-500"></i>
                                <i className="fa-solid fa-trash cursor-pointer hover:text-gray-500"></i>
                            </div>
                        </div> 
                    </div>
                ))}
            </div>
        </div>
    )
}