from domain.event import Event
from repository.repository import Repository

import datetime
import qrcode

class EventService:
    def __init__(self, repository: Repository):
        """
        Constructor for EventService class
        :param repository: event repository (Repository)
        :return:
        """
        self.__repository = repository

    def add_event(self, id, name, city, participants, slots, start, finish, website):
        """
        Adds an event to the event list if it doesn't already exist
        :param id: id of the event (string)
        :param name: name of the event (string)
        :param city: city of the event (string)
        :param participants: number of participants (int)
        :param slots: number of slots (int)
        :param start: start date  (datetime)
        :param finish: finish date (datetime)
        :param website: website of the event (string)
        :return:
        """
        event = Event(id, name, city, participants, slots, start, finish, website)
        self.__repository.add(event)

    def event_exists(self, id):
        """
        Checks if the event with a given id exists
        :param id: id of the event (string)
        :return: True if the event exists, False otherwise
        """
        return self.__repository.find_position(Event(id), 0, 0, 0, 0, 0, 0) is not None

    def delete_event(self, id):
        """
        Deletes an event with a given id
        :param id: id of the event (string)
        :return:
        """
        event = Event(id, 0, 0, 0, 0, 0, 0, 0)
        self.__repository.delete(event)

    def edit_event(self, id, name, city, participants, slots, start, finish, website):
        """
        Edits an event with a given id
        :param id: id of the event (string)
        :param name: name of the event (string)
        :param city: city of the event (string)
        :param participants: number of participants (int)
        :param slots: number of slots (int)
        :param start: start date  (datetime)
        :param finish: finish date (datetime)
        :param website: website of the event (string)
        :return:
        """
        event = Event(id, name, city, participants, slots, start, finish, website)
        self.__repository.update(event)

    def get_all_events(self):
        """
        Returns the list containing all the events
        :return: The list of all the events (list)
        """
        return self.__repository.get_all()

    def get_city_events(self, city):
        """
        Returns the list containing all the events from a given city
        :param city: city of the event (string)
        :return: The list of all the events from a given city (list)
        """
        event_list = self.__repository.get_all()
        city_events = []
        for event in event_list:
            if event.get_city() == city:
                city_events.append(event)
        return city_events

    def get_events_with_participants(self):
        """
        Gets all the events with participants and sorts descending by the number of participants
        :return: the events with participants (list)
        """
        events = self.__repository.get_all()
        filtered_events = []
        for event in events:
            if event.get_participants() != 0:
                filtered_events.append(event)
        filtered_events.sort(key=lambda event: event.get_participants(), reverse=True)
        return filtered_events

    def generate_qr_code(self, id):
        """
        Generates a QR code for a given event
        :param id: id of the event (string)
        :return:
        """
        event = self.__repository.find(Event(id, 0, 0, 0, 0, 0, 0, 0))
        img = qrcode.make(event.get_website())
        img.save('qr_code.png')

    def get_events_within_7_days(self):
        """
        Gets all the events within 7 days and sorts ascending by slots
        :return: the events within 7 days (list)
        """
        events = self.__repository.get_all()
        filtered_events = []
        for event in events:
            if event.get_start() <= datetime.datetime.now() + datetime.timedelta(days=7):
                filtered_events.append(event)
        events.sort(key=lambda event: event.get_slots())
        return filtered_events

    def get_events_in_month(self, date):
        """
        Shows events in a given month in a descending order based on days duration
        :param date: date of the event (datetime)
        :return: the events in a given month (list)
        """
        events = self.__repository.get_all()
        filtered_events = []
        for event in events:
            if event.get_start().month == date.month and event.get_start().year == date.year:
                filtered_events.append(event)
        filtered_events.sort(key=lambda event: (event.get_finish() - event.get_start()).days, reverse=True)
        return filtered_events