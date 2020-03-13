# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, inventory = []):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory
    def travel(self, direction):
        if getattr(self.current_room, f"{direction}_to"):
            self.current_room = getattr(self.current_room, f"{direction}_to")
            print(self.current_room)
        else:
            print(f"You cannot move in that direction.\n")
    def look(self):
        if len(self.current_room.item) == 0:
            print("Nothing was found.")
        else:
            for item in self.current_room.item:
                print(f"You found a '{item.name}' {item.description}.")
            return print("If you would like to pick up the item, please enter 'get' and the name of the item.")
    def pickup(self, item):
        self.inventory.append(item)
        print(f"You picked the item and it has been added to your inventory.")
    def dropped(self, item):
        print(f"You dropped {item}")