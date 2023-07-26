class Participant:
    def __init__(self, name, profile_picture, enlisted_events):
        self.__name = name
        self.__profile_picture = profile_picture
        self.__enlisted_events = enlisted_events

    def get_name(self):
        return self.__name

    def is_enlisted(self, event):
        return event.get_id() in self.__enlisted_events

    def __str__(self):
        return f"""Name: {self.__name}
Profile picture: {self.__profile_picture}
Enlisted events: {self.__enlisted_events}"""

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.get_name() == other.get_name()