# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room="outside", victory=False):
        self.name = name
        self.current_room = current_room
        self.victory = victory

    def __str__(self):
        return f"{self.name} you are in the {self.current_room}"

    def get_name(self):
        return self.name

    def get_location(self):
        return self.current_room
    
    def get_victory(self):
        return self.victory