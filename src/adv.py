from room import Room
from player import Player

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_name = input(f"Please enter your name: ")
player = Player(player_name, room['outside'])

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

while True:
    room = player.current_room
    user_input = input(f"\n{player_name}, please enter one of the following commands:\nn: North, s: South, e: East, w: West, q: Quit\n")
    print(f"\n{room.name}")
    print(f"{room.description}\n")
    
    if user_input == "n":
        if room.n_to is not None:
            player.current_room = room.n_to
        else:
            print("Cannot go North.")
    elif user_input == "s":
        if room.s_to is not None:
            player.current_room = room.s_to
        else:
            print("Cannot go South.")
    elif user_input == "e":
        if room.e_to is not None:
            player.current_room = room.e_to
        else:
            print("Cannot go East.")
    elif user_input == "w":
        if room.w_to is not None:
            player.current_room = room.w_to
        else:
            print("Cannot go West.")
    elif user_input == "q":
        print("Quitting")
        break
    else:
        print("Please enter a valid command.")