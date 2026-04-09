import { useState, useEffect } from "react";
import api from "../../services/api";

export default function NewDeckModal(props) {

    const [name, setName] = useState("");

    async function handleCreate() {
        try {
            const response = await api.post("/decks/user/1", { name : name });
            props.onDeckCreated(response.data);
            alert("Deck criado com sucesso");
            setName("");
            props.onClose();
        } catch (err) {
            alert("Falha ao criar deck: " + err.message);
        }
    } 

    return (
        <div className="w-full h-screen bg-black/80 fixed top-0 left-0 flex items-center justify-center">
            <div className="w-[50%] h-content bg-white p-5 rounded-md flex flex-col">
                <div className="flex place-content-between">
                    <h2 className="font-semibold mb-3">Novo Deck</h2>
                    <button
                        onClick={props.onClose}
                        className="cursor-pointer">X</button>
                </div>
                <label>Título</label>
                <input type="text" 
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    className="border-2 border-gray-400 p-1 mt-1 rounded-md focus:outline-2 focus:outline-orange-500" 
                    placeholder="Nome do deck" />
                <div className="flex mt-2 justify-end">
                    <button
                        onClick={props.onClose}
                        className="bg-gray-300 rounded-md px-3 py-1 mr-2 cursor-pointer"
                    >
                        Cancelar
                    </button>
                    <button onClick={handleCreate} className="bg-orange-300 rounded-md px-3 py-1 cursor-pointer">Criar</button>
                </div>
                
            </div>
        </div>
    )
}