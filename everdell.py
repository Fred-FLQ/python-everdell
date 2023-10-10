# Classes setup
# class Resource:
#     def __init__(self, type):
#         self.type = type

#     def __repr__(self):
#         ### IMPROVE: explain what is the resource mainly used for in description
#         if self.type.lower() == "galet":
#             return f"Cette ressource est un {self.type.lower()}."
#         else:
#             return f"Cette ressource est une {self.type.lower()}."

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
        self.cards_in_hand = []

    # Use repr method to display Town's Dashboard
    def __repr__(self):
        town_repr = (
            f"Here is the dashboard for {self.name}'s town.\n"
            f"Currently, you have {len(self.constructions)} constructions and {len(self.critters)} critters living in your town.\n"
            f"You also have {self.workers} workers and the following resources at your disposal:\n"
        )

        # This could be handled a different way through a dedicated function maybe?
        # Could then use it for constructions and critters in town_repr.
        for resource, quantity in self.resources.items():
            if quantity > 1 and resource == "Berry":
                town_repr += f"- {quantity} Berries\n"
            elif quantity > 1 and not resource == "Berry":
                town_repr += f"- {quantity} {resource}s\n"
            else:
                town_repr += f"- {quantity} {resource}\n"

        return town_repr

    def place_worker():
        pass


class Critter:  # For future version, need to learn how to create instances from a csv file or a database
    def __init__(self, name, type, cost, points, unique=False):
        self.name = name
        self.type = type
        self.cost = cost
        self.points = points
        self.unique = unique

    def __repr__(self):
        critter_repr = (
            f"The {self.name} card is a {self.type} card. It costs:\n"
        )

        # definitely needs a global function to handle plural
        for resource, quantity in self.cost.items():
            critter_repr += f"- {quantity} {resource}\n"

        return critter_repr


class Construction:
    def __init__(self, name, cost, points, unique=False):
        self.name = name
        self.cost = cost
        self.points = points
        self.unique = unique


##################
# Game mechanics #
##################

# intro_logo = r"""
# ░█▀█░█░█░▀█▀░█░█░█▀█░█▀█░░░█▀▀░█░█░█▀▀░█▀▄░█▀▄░█▀▀░█░░░█░░
# ░█▀▀░░█░░░█░░█▀█░█░█░█░█░░░█▀▀░▀▄▀░█▀▀░█▀▄░█░█░█▀▀░█░░░█░░
# ░▀░░░░▀░░░▀░░▀░▀░▀▀▀░▀░▀░░░▀▀▀░░▀░░▀▀▀░▀░▀░▀▀░░▀▀▀░▀▀▀░▀▀▀
# """
# print(intro_logo)
# player1_name = input("Ready to play Python Everdell? What is your name?")
# player2_name = input(
#     "Welcome " + str(player1_name) + "! What is the name of your opponent?"
# )

# player1_town = Town(player1_name)
# player2_town = Town(player2_name)
# print(player1_town)
# print(player2_town)

judge = Critter("Judge", "Governance", {"Berry": 3, "Pebble": 1}, 2, True)
print(judge)