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


class Town:
    def __init__(self, name):
        self.name = name
        self.workers = 2
        self.total_points = 0
        self.constructions = []
        self.critters = []
        self.resources = {"Twig": 0, "Resin": 0, "Pebble": 0, "Berry": 0}

    def __repr__(self):
        message = (
            f"Here is the dashboard for {self.name}'s town.\n"
            f"Currently, you have {len(self.constructions)} constructions and {len(self.critters)} critters living in your town.\n"
            f"You also have {self.workers} workers and the following resources at your disposal:\n"
        )

        # This could be handled a different way through a dedicated function maybe?
        # Could then use it for constructions and critters in message.
        for resource, quantity in self.resources.items():
            if quantity > 1 and resource == "Berry":
                message += f"- {quantity} Berries\n"
            elif quantity > 1 and not resource == "Berry":
                message += f"- {quantity} {resource}s\n"
            else:
                message += f"- {quantity} {resource}\n"

        return message

    def place_worker():
        pass


class Construction:
    def __init__(self, name, cost, points, unique=False):
        self.name = name
        self.cost = cost
        self.points = points
        self.unique = unique


class Critter:
    def __init__(self, name, type, cost, points, unique=False):
        pass


# Game mechanics

intro_logo = r"""
░█▀█░█░█░▀█▀░█░█░█▀█░█▀█░░░█▀▀░█░█░█▀▀░█▀▄░█▀▄░█▀▀░█░░░█░░
░█▀▀░░█░░░█░░█▀█░█░█░█░█░░░█▀▀░▀▄▀░█▀▀░█▀▄░█░█░█▀▀░█░░░█░░
░▀░░░░▀░░░▀░░▀░▀░▀▀▀░▀░▀░░░▀▀▀░░▀░░▀▀▀░▀░▀░▀▀░░▀▀▀░▀▀▀░▀▀▀
"""
print(intro_logo)
player1_name = input("Ready to play Python Everdell? What is your name?")
player2_name = input(
    "Welcome " + str(player1_name) + "! What is the name of your opponent?"
)

player1_town = Town(player1_name)
player2_town = Town(player2_name)
print(player1_town)
print(player2_town)
