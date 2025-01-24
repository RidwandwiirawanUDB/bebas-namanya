from university import University

class Room:
    def __init__(self, room_number, capacity):
        self.room_number = room_number
        self.capacity = capacity

    def __str__(self):
        return f"Room {self.room_number}, Capacity: {self.capacity}"

    @classmethod
    def add_room(cls):
        building_name = input("Enter the name of the building to add a room: ")
        room_number = input("Enter room number: ")
        capacity = int(input("Enter room capacity: "))

        # Find the building where the room will be added.
        building = next((b for b in University.buildings if b.name == building_name), None)
        if building:
            building.rooms.append(cls(room_number, capacity))
            print(f"Room {room_number} added successfully to {building_name}!\n")
        else:
            print(f"Building '{building_name}' not found. Room not added.\n")
