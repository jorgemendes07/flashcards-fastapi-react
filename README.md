# Flashcards App

Este projeto é uma aplicação voltada para aprendizado através de decks de flashcards.

A proposta é permitir que usuários criem seus próprios decks de estudo, compostos por cards com perguntas e respostas, e utilizem sessões de treino para reforçar o conhecimento.

O foco principal da aplicação é simplicidade, autonomia do usuário e prática ativa.

---

## Objetivo

Fornecer uma ferramenta onde o usuário:

- Cria seus próprios decks de estudo
- Organiza conteúdos por temas
- Pratica através de sessões de treino
- Avalia seu nível de domínio sobre cada card

A responsabilidade pelo aprendizado é do próprio usuário.  
O sistema apenas facilita o processo.

---

## Conceito de Funcionamento

Cada deck é composto por cards, e cada card possui:

- Um termo ou pergunta na frente
- Uma resposta no verso

Durante uma sessão de treino:

1. Os cards são apresentados de forma aleatória
2. O usuário responde mentalmente
3. O usuário classifica o card como:
   - Fácil
   - Médio
   - Difícil

Ao final da sessão, o card recebe, ou atualiza, sua classificação de dificuldade.  
Essa classificação permanece até que o usuário a altere em uma nova sessão.

---

## Regras de Uso

- Cada usuário gerencia apenas seus próprios decks
- Cards pertencem exclusivamente ao deck onde foram criados
- Não há limite para criação de decks
- Caso um usuário seja removido, seus decks também deixam de existir
- Caso um deck seja removido, seus cards também deixam de existir