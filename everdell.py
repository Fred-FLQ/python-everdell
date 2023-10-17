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


class Town:
    def __init__(self, name):
        self.name = name
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
            f"In {self.name}'s town, there are currently {len(self.constructions)} constructions and {len(self.critters)} critters.\n"
            f"It represents {self.total_points} Victory Points.\n"
            f"There are also {self.workers} workers and the following resources available:\n"
        )

        # This could be handled a different way through a dedicated global function maybe?
        # Could then use it in every sentences... -_-
        for resource, quantity in self.resources.items():
            if quantity > 1 and resource == "Berry":
                town_dashboard += f"- {quantity} Berries\n"
            elif quantity > 1 and not resource == "Berry":
                town_dashboard += f"- {quantity} {resource}s\n"
            else:
                town_dashboard += f"- {quantity} {resource}\n"

        print(town_dashboard)
        self.action_menu()
        self.process_user_input()

    # For this version of the game, each player will get cards only once
    def first_cards_gen(self, cards_data):
        # Deal 5 cards to each player
        for cards_count in range(5):
            if len(cards_data) > 0:
                # Randomize and pop cards that get into players' hand
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

    # Display possible player's actions
    def action_menu(self):
        print("Choose an action:")
        print("1. Display Town's Dashboard")
        print("2. Display cards in hand")
        print("3. Place a worker")

    # Process player's choice
    def process_user_input(self):
        user_input = input(f"{self.name}, what do you wanna do next? ")
        if user_input == "1":
            self.town_dashboard()
        elif user_input == "2":
            if len(self.cards_in_hand) > 0:
                print(f"{self.name}, here are the cards you have in hand:\n")
                print(self.cards_in_hand)
                self.play_card(input(f"{self.name}, which card do you wanna play? "))
            else:
                print(f"{self.name}, you don't have any cards in your hand.")
                self.action_menu()
                self.process_user_input()
        elif user_input == "3":
            self.place_worker()
        else:
            print(
                "Your choice is not valid. Input the number of the action you wanna do."
            )
            self.action_menu()
            self.process_user_input()

    # Check if played card valid, remove it from player's hand and add it to town
    def play_card(self, card):
        if card.lower() in self.cards_in_hand:
            print(f"You just played {card.title()}.")
            played_card = self.cards_in_hand[card.lower()]
            # Checking type of card to add to the right category
            if played_card.deck == "critter":
                self.critters.append(self.cards_in_hand.pop(card.lower()))
            elif played_card.deck == "construction":
                self.constructions.append(self.cards_in_hand.pop(card.lower()))
            # Adding card's points to Town's Victory Points
            self.total_points += played_card.points
            print(f"You now have {len(self.critters)} critters and {len(self.constructions)} constructions in your town. It represents {self.total_points} Victory Points.")
        else:
            print("You don't have this card in your hand.")
            self.play_card(input("Please choose an other card. "))
        self.action_menu()
        self.process_user_input()

class Card:
    def __init__(self, deck, name, type, cost, points, unique=False):
        self.deck = deck
        self.name = name
        self.type = type
        self.cost = cost
        self.points = points
        self.unique = unique

    def __repr__(self):
        card_repr = f"The {self.name.title()} is a {'unique' if self.unique else ''} {self.deck.title()}. It is a {self.type} card that gives {self.points} Victory Points. It costs:\n"

        # definitely needs a global function to handle plural
        for item in self.cost:
            quantity = item["quantity"]
            resource = item["resource"]
            card_repr += f"- {quantity} {resource.title()}\n"

        return card_repr


##################
# Game mechanics #
##################

intro_logo = r"""
░█▀█░█░█░▀█▀░█░█░█▀█░█▀█░░░█▀▀░█░█░█▀▀░█▀▄░█▀▄░█▀▀░█░░░█░░
░█▀▀░░█░░░█░░█▀█░█░█░█░█░░░█▀▀░▀▄▀░█▀▀░█▀▄░█░█░█▀▀░█░░░█░░
░▀░░░░▀░░░▀░░▀░▀░▀▀▀░▀░▀░░░▀▀▀░░▀░░▀▀▀░▀░▀░▀▀░░▀▀▀░▀▀▀░▀▀▀
"""
print(intro_logo)
player1_name = input("Ready to play Python Everdell?\nWhat is Player 1's name? ")
player2_name = input(
    "Welcome " + str(player1_name) + "!\nWhat is the Player 2's name? "
)

player1_town = Town(player1_name)
player2_town = Town(player2_name)


player1_town.action_menu()
player1_town.process_user_input()

# Check deck length (uncomment for test only)
# print("lenght of deck:" + str(len(cards_data)))