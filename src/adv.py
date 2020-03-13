from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Items

item = {
    'flashlight': Item("flashlight", "that lights up the room"),
    'silver': Item("pouch", "thats filled with silver"),
    'map': Item("map", "with a location of a different treasure chest")
}

# Add items to rooms

room['narrow'].item.append(item['flashlight'])
room['treasure'].item.append(item['silver'])
room['treasure'].item.append(item['map'])

def get_item(item_name, item_list):
    for index, find_item in enumerate(item_list):
        return index if find_item.name.lower() == item_name.lower() else None
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(input("Please enter your name: "), room['outside'])
print(player.current_room)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

valid_directions = ("n", "s", "e", "w")

while True:
    cmd = input(f"\n{player.name}, please select a command: ")
    if cmd == "q":
        print(f"\nGoodbye, {player.name}!")
        exit(0)
    elif cmd in valid_directions:
        player.travel(cmd)
    elif cmd == "l":
        player.look()
    elif len(cmd.split()) == 2:
        action = cmd.split()[0].lower()
        item_name = cmd.split()[1].lower()
        room_items = player.current_room.item
        if (action == "get" or "take") and get_item(item_name, room_items) is not None:
            items = get_item(item_name, room_items)
            item_got = room_items[0]
            item_got.get_item()
            room_items.remove(item_got)
            player.inventory.append(item_got)
        if action == "drop" and get_item(item_name, player.inventory) is not None:
            items = get_item(item_name, player.inventory)
            item_got = player.inventory[items]
            item_got.drop_item()
            player.inventory.remove(item_got)
            room_items.append(item_got)
    elif cmd == "i":
        if len(player.inventory) == 0:
            print("You have no items.")
        else:
            print("You have the following item(s):")
            for player_items in player.inventory:
                print(player_items)
            print("If you would like to drop an item, please enter 'drop' and the name of the item.")
    else:
        print(f"\n{player.name}, please enter a valid command.")