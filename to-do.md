# To Do List

## General items

- [x] First draft of project scope
- [x] First iteration of classes mapping and relationships
- [x] Iniate and update To do list in Readme.md
- [ ] **FUTURE VERSION** Add a global function to handle plural
- [x] Decided to try to store and access cards data from a json file (SCOPE CREEP, here you are!!)
- [X] Add more cards info to json file

## Classes

### Game Class

*Note: This class was added later on as a refactoring of the code. It was mainly triggered by the necessity to handle players' taking turn in a modular and flexible way for future features. This new method didn't really belong in any of the existing classes and some of the existing classes methods didn't really belong to those classes either.*

- [x] Game class:
    - [x] Initiate class with player's name input in mind + active player
    - [x] Create players' town instances on init (move & refacto code from execution part of the program)
    - [x] Move action_menu() method
    - [x] Move process_user_input() method
    - [x] Adapt Town class __init__() method and others to new Game class
    - [ ] ?? Move cards dealing and play_card() method in Game class??

- [ ] Player's actions Menu & User Input Processing
    - [x] Add a "Stop playing" option and associated function
    - [X] Display cards in hand and possibility to play a card
    - [ ] **FUTURE VERSION** Player action: place a worker to get resources (*dependance: Location class*)

- [x] Switch_player() method
    - [x] Call switch_player() method where relevant

### Town Class

- [x] Player's Town:
    - [x] Add and display Town's name
    - [x] Add and display Town's Dashboard with number of constructions, critters, workers and resources.
    - [x] Add and display cards in hand
    - [x] Add different cards to player 1 hand and player 2 hand
    - [x] Randomize cards dealt to players

- [ ] Player's actions in town:

    - [x] Player action: display town's dashboard
    - [ ] Player action: play a card in hand
        - [x] Play a card without resources limit
        - [ ] **FUTURE VERSION** Add a resource condition to be able to play a card

### Card Class

- [x] Card class
    - [x] Init constructor
    - [x] Repr for tests and later UI
    - [x] Merge older Critter and Construction class into this one

### Location Class