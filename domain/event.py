class Event:
    def __init__(self, id, name, city, participants, slots, start, finish, website):
        self.__id = id
        self.__name = name
        self.__city = city
        self.__participants = participants
        self.__slots = slots
        self.__start = start
        self.__finish = finish
        self.__website = website

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_city(self):
        return self.__city

    def get_participants(self):
        return self.__participants

    def set_participants(self, participants):
        self.__participants = participants

    def get_slots(self):
        return self.__slots

    def get_start(self):
        return self.__start

    def get_finish(self):
        return self.__finish

    def get_website(self):
        return self.__website

    def __str__(self):
        return f"""ID: {self.__id}
Name: {self.__name}
City: {self.__city}
Participants: {self.__participants}
Slots: {self.__slots}
Start: {self.__start}
Finish: {self.__finish}
Website: {self.__website}"""

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.get_id() == other.get_id()