##################
#  Imports & Co  #
##################

import random

import json

with open("cards_deck.json") as cards_deck:
    cards_data = json.load(cards_deck)

# Check deck length (uncomment for test only)
# print("lenght of deck:" + str(len(cards_data)))

##################
#   Game Setup   #
##################

# New class to handle game mechanics
class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.active_player = self.player1

        # Create players' town instances
        self.player1_town = Town(player1, self)
        self.player2_town = Town(player2, self)

        self.action_menu()
        self.process_user_input()
    
    def switch_player(self):
        if self.active_player == self.player1:
            self.active_player = self.player2
        else:
            self.active_player = self.player1

    # Display possible player's actions
    def action_menu(self):
        print(f"\n{self.active_player}, what do you wanna do next?")
        print("1. Display Town's Dashboard")
        print("2. Display cards in hand")
        # print("3. Place a worker")
        print("4. Stop playing")
    
     # Process player's choice depending on active player
    def process_user_input(self):
        user_input = input(f"{self.active_player}, choose an action: ")
        if user_input == "1":
            if self.active_player == self.player1:
                self.player1_town.town_dashboard()
            else:
                self.player2_town.town_dashboard()
        elif user_input == "2":
            if self.active_player == self.player1:
                if len(self.player1_town.cards_in_hand) > 0:
                    cards_hand_display = (
                        f"\n{self.active_player}, here are the cards you have in hand:\n"
                    )
                    for card, description in self.player1_town.cards_in_hand.items():
                        cards_hand_display += f"- {card.upper()}: {description}\n"
                    print(cards_hand_display)
                    self.player1_town.play_card(input(f"{self.active_player}, which card do you wanna play? "))
                else:
                    print(f"{self.active_player}, you don't have any cards in your hand.")
                    self.action_menu()
                    self.process_user_input()
            if self.active_player == self.player2:
                if len(self.player2_town.cards_in_hand) > 0:
                    cards_hand_display = (
                        f"\n{self.active_player}, here are the cards you have in hand:\n"
                    )
                    for card, description in self.player2_town.cards_in_hand.items():
                        cards_hand_display += f"- {card.upper()}: {description}\n"
                    print(cards_hand_display)
                    self.player2_town.play_card(input(f"{self.active_player}, which card do you wanna play? "))
                else:
                    print(f"{self.active_player}, you don't have any cards in your hand.")
                    self.action_menu()
                    self.process_user_input()
        # Not available yet
        # elif user_input == "3":
        #     self.place_worker()
        elif user_input == "4":
            exit()
        else:
            print(
                "Your choice is not valid. Input the number of the action you wanna do."
            )
            self.action_menu()
            self.process_user_input()

class Town:
    def __init__(self, name, game):
        self.name = name
        self.game = game
        self.workers = 2
        self.total_points = 0
        self.constructions = []
        self.critters = []
        self.resources = {"Twig": 0, "Resin": 0, "Pebble": 0, "Berry": 0}
        self.cards_in_hand = {}

        self.first_cards_gen(cards_data)

    # Simplified repr to stick to Python's principles
    def __repr__(self):
        town_repr = (
            f"In {self.name}'s town, there are currently {len(self.constructions)} constructions and {len(self.critters)} critters.\n"
            f"{self.name} has {self.total_points} Victory Points."
        )

        return town_repr

    # Dedicated method to display Town's Dashboard
    def town_dashboard(self):
        town_dashboard = (
            f"\nIn {self.name}'s town, there are currently {len(self.constructions)} constructions and {len(self.critters)} critters.\n"
            f"It represents {self.total_points} Victory Points.\n"
            f"There are also {self.workers} workers and the following resources available:\n"
        )

        # This could be handled a different way through a dedicated global function maybe?
        # Could then use it in every sentences... -_-;
        for resource, quantity in self.resources.items():
            if quantity > 1 and resource == "Berry":
                town_dashboard += f"- {quantity} Berries\n"
            elif quantity > 1 and not resource == "Berry":
                town_dashboard += f"- {quantity} {resource}s\n"
            else:
                town_dashboard += f"- {quantity} {resource}\n"

        print(town_dashboard)
        self.game.action_menu()
        self.game.process_user_input()

    # For this version of the game, each player will get cards only once
    def first_cards_gen(self, cards_data):
        # Deal 5 cards to each player
        for cards_count in range(5):
            if len(cards_data) > 0:
                # Randomize and pop cards from deck
                i = random.randint(0, len(cards_data)-1)
                card = Card(
                        cards_data[i]["deck"],
                        cards_data[i]["name"],
                        cards_data[i]["type"],
                        cards_data[i]["cost"],
                        cards_data[i]["points"],
                        cards_data[i]["unique"],
                    )
                self.cards_in_hand[cards_data[i]["name"]] = card
                cards_data.pop(i)

        # return cards_in_hand


    # Check if played card is valid, remove it from player's hand and add it to town
    def play_card(self, card):
        if card.lower() in self.cards_in_hand:
            print(f"\n{self.name}, you just played {card.upper()}.")
            played_card = self.cards_in_hand[card.lower()]
            # Checking type of card to add to the right category
            if played_card.deck == "critter":
                self.critters.append(self.cards_in_hand.pop(card.lower()))
            elif played_card.deck == "construction":
                self.constructions.append(self.cards_in_hand.pop(card.lower()))
            # Adding card's points to Town's Victory Points
            self.total_points += played_card.points
            print(f"You now have {len(self.constructions)} constructions and {len(self.critters)} critters in your town. It represents {self.total_points} Victory Points.")
        else:
            print("You don't have this card in your hand.")
            self.play_card(input("Please choose another card: "))
        self.game.switch_player()
        self.game.action_menu()
        self.game.process_user_input()

# Generic class to handle any type of cards
class Card:
    def __init__(self, deck, name, type, cost, points, unique=False):
        self.deck = deck
        self.name = name
        self.type = type
        self.cost = cost
        self.points = points
        self.unique = unique

    def __repr__(self):
        card_repr = f"The {self.name.title()} is a {'unique' if self.unique else ''} {self.deck.title()}. It is a {self.type} card that gives {self.points} Victory Points. It costs: "

        # definitely needs a global function to handle plural
        for item in self.cost:
            quantity = item["quantity"]
            resource = item["resource"]
            card_repr += f"- {quantity} {resource.title()} "

        return card_repr


##################
#  Main program  #
##################

intro_logo = r"""
░█▀█░█░█░▀█▀░█░█░█▀█░█▀█░░░█▀▀░█░█░█▀▀░█▀▄░█▀▄░█▀▀░█░░░█░░
░█▀▀░░█░░░█░░█▀█░█░█░█░█░░░█▀▀░▀▄▀░█▀▀░█▀▄░█░█░█▀▀░█░░░█░░
░▀░░░░▀░░░▀░░▀░▀░▀▀▀░▀░▀░░░▀▀▀░░▀░░▀▀▀░▀░▀░▀▀░░▀▀▀░▀▀▀░▀▀▀
"""
print(intro_logo)
player1_name = input("Ready to play Python Everdell?\nWhat is your name? ")
player2_name = input(
    "\nWelcome " + str(player1_name) + "!\nWhat is your opponent's name? "
)
current_game = Game(player1_name, player2_name)
