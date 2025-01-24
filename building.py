from university import University

class Building:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.rooms = []  # Each building holds its own list of rooms.

    def __str__(self):
        return f"Building: {self.name}, Address: {self.address}"

    @classmethod
    def add_building(cls):
        name = input("Enter building name: ")
        address = input("Enter building address: ")
        University.buildings.append(cls(name, address))
        print("Building added successfully!\n")
