# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, victory=False):
        self.name = name
        self.current_room = current_room
        self.victory = victory
        self.player_items = []

    def __str__(self):
        # return f"{self.name} you are in the {self.current_room}"
        return f"{self.name}"

    # def get_name(self):
    #     return self.name
    # don't need after refactor?
    def set_location(self, room):
        if room != None:
            self.current_room = room
            return self.current_room
        else:
            return -1