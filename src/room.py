# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def __str__(self):
        return_string = f"\n{self.name}\n{self.description}\n\nCommands: {self.get_exits_string()}\n"
        return return_string
    def get_exits_string(self):
        exits = ["q to QUIT"]
        if self.n_to:
            exits.append("n to go NORTH")
        if self.s_to:
            exits.append("s to go SOUTH")
        if self.e_to:
            exits.append("e to go EAST")
        if self.w_to:
            exits.append("w to go WEST")
        return exits