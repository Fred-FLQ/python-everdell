# To Do List

## General items

- [x] First draft of project scope
- [x] First iteration of classes mapping and relationships
- [x] Iniate and update To do list in Readme.md
- [ ] **NEW** Add a global function to handle plural
- [x] Decided to try to store and access cards data from a json file (SCOPE CREEP, here you are!!)
- [ ] Add more cards info to json file

## Classes

### Town Class

- [ ] Create Player's Town:
    - [x] Add and display Town's name
    - [x] Add and display Town's Dashboard with number of constructions, critters, workers and resources.
    - [x] Add and display cards in hand
    - [ ] Add different cards to player 1 hand and player 2 hand
    - [ ] Randomize cards dealt to players

- [ ] Add Player's actions to Town:
    - [ ] Player action: display town's constructions
    - [ ] Player action: display town's critters
    - [ ] Player action: display number of Victory Points
    - [ ] Player action: place a worker to get resources (*dependance: Location class*)
    - [x] Player action: display town's dashboard
    - [ ] Player action: display cards in hand and play a card
        - [x] Play a card without resources limit
        - [ ] Add a resource condition to be able to play a card

### Card Class

- [ ] Create Card class Critters
    - [x] Init constructor
    - [x] Repr for tests and later UI
    - [x] Merge older Critter and Construction class into this one



### Location Class