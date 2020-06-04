# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, room_items=[]):
        self.name = name
        self.description = description
        self.room_items = room_items
       

    def __str__(self):
        # for empty item lsit
        if self.room_items == []:
            return f"{self.name}. {self.description}."
        else:
            items = ""
            for item in self.room_items:
                items += item.name + " " + item.description + " "
            return f"{self.name}. {self.description}. Look, there are some old things on the ground: {items}"

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description