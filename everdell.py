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
        return f"This is {self.name}'s town."

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


stone = Resource("GALETTT")
print(stone)
