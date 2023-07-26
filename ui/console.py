from domain.event import Event
from service.event_service import EventService
from service.participant_service import ParticipantService

import datetime

class ConsoleUI:
    def __init__(self, event_service: EventService, participant_service: ParticipantService):
        self.__event_service = event_service
        self.__participant_service = participant_service

    def __start_menu(self):
        print("\nWelcome to TIPD Association events application\n\n"
              "Please pick an application mode:\n"
              "1. Organiser mode\n"
              "2. Participant mode\n"
              "0. Exit\n")

    def __organiser_menu(self):
        print("\nOrganiser menu\n\n"
              "Options:\n"
                "1. Add event\n"
                "2. Delete event\n"
                "3. Edit event\n"
                "4. Show all events\n"
                "5. Show all events in a city\n"
                "6. Show event participants\n"
                "7. Show all events with participants in a descending order\n"
                "8. Generate QR code for event\n"
                "9. Back\n"
                "0. Exit\n")

    def __participant_menu(self):
        print("\nParticipant menu\n\n"
              "Options:\n"
              "1. Show all events\n"
              "2. Enlist to event\n"
              "3. View events starting in 7 days in a ascending order based on max slots\n"
              "4. View events starting in given month in a descending order based on duration\n"
              "5. Back\n"
              "0. Exit\n")

    def __validate_participants(self, participants: str):
        try:
            int(participants)
        except Exception:
            raise ValueError("Participants is not a number!")

    def __validate_slots(self, slots: str):
        try:
            int(slots)
        except Exception:
            raise ValueError("Slots is not a number!")

    def __validate_start(self, start: str):
        try:
            datetime.datetime.strptime(start, '%d-%m-%Y')
        except Exception:
            raise ValueError("Start is not a valid date!")

    def __validate_finish(self, finish: str):
        try:
            datetime.datetime.strptime(finish, '%d-%m-%Y')
        except Exception:
            raise ValueError("Finish is not a valid date!")

    def __add_event(self):
        id = input("ID: ")
        name = input("Name: ")
        city = input("City: ")
        participants = input("Participants: ")
        slots = input("Slots: ")
        start = input("Start Date (format 30-05-2007): ")
        finish = input("Finish Date (format 30-05-2007): ")
        website = input("Website: ")

        self.__validate_participants(participants)
        self.__validate_slots(slots)
        self.__validate_start(start)
        self.__validate_finish(finish)

        self.__event_service.add_event(id, name, city, int(participants), int(slots), datetime.datetime.strptime(start, '%d-%m-%Y'), datetime.datetime.strptime(finish, '%d-%m-%Y'), website)

    def __delete_event(self):
        id = input("Event ID: ")

        self.__event_service.delete_event(id)

    def __edit_event(self):
        id = input("Event ID: ")
        name = input("New name: ")
        city = input("New city: ")
        participants = input("New participants: ")
        slots = input("New slots: ")
        start = input("New start date (format 30-05-2007): ")
        finish = input("New finish date (format 30-05-2007): ")
        website = input("New website: ")

        self.__validate_participants(participants)
        self.__validate_slots(slots)
        self.__validate_start(start)
        self.__validate_finish(finish)

        self.__event_service.edit_event(id, name, city, int(participants), int(slots), datetime.datetime.strptime(start, '%d-%m-%Y'), datetime.datetime.strptime(finish, '%d-%m-%Y'), website)

    def __show_all_events(self):
        for event in self.__event_service.get_all_events():
            print(f"{event}\n")

    def __show_city_events(self):
        city = input("City: ")

        for event in self.__event_service.get_city_events(city):
            print(f"{event}\n")

    def __show_event_participants(self):
        id = input("Event ID: ")

        for participant in self.__participant_service.get_event_participants(id):
            print(f"{participant}\n")

    def __show_events_with_participants(self):
        for event in self.__event_service.get_events_with_participants():
            print(f"{event}\n")

    def __generate_qr_code(self):
        id = input("Event ID: ")

        self.__event_service.generate_qr_code(id)

    def __enlist_to_event(self):
        id = input("Event ID: ")
        name = input("Participant name: ")
        profile_picture = input("Participant profile picture: ")

        self.__participant_service.enlist_to_event(id, name, profile_picture)

    def __show_events_within_7_days(self):
        for event in self.__event_service.get_events_within_7_days():
            print(f"{event}\n")

    def __show_events_in_month(self):
        date = input("Date (format 05-2007): ")
        try:
            datetime.datetime.strptime(date, '%m-%Y')
        except Exception:
            raise ValueError("Date is not a valid date!")

        for event in self.__event_service.get_events_in_month(datetime.datetime.strptime(date, '%m-%Y')):
            print(f"{event}\n")

    def run(self):
        while True:
            self.__start_menu()
            try:
                mode = int(input("Choose application mode: ").strip())
                if mode == 0:
                    return
                elif mode == 1:
                    while True:
                        self.__organiser_menu()
                        command = int(input("Choose command: ").strip())
                        if command == 0:
                            return
                        elif command == 1:
                            self.__add_event()
                        elif command == 2:
                            self.__delete_event()
                        elif command == 3:
                            self.__edit_event()
                        elif command == 4:
                            self.__show_all_events()
                        elif command == 5:
                            self.__show_city_events()
                        elif command == 6:
                            self.__show_event_participants()
                        elif command == 7:
                            self.__show_events_with_participants()
                        elif command == 8:
                            self.__generate_qr_code()
                        elif command == 9:
                            break
                        else:
                            print("Invalid command!")
                elif mode == 2:
                    while True:
                        self.__participant_menu()
                        command = int(input("Choose command: ").strip())
                        if command == 0:
                            return
                        elif command == 1:
                            self.__show_all_events()
                        elif command == 2:
                            self.__enlist_to_event()
                        elif command == 3:
                            self.__show_events_within_7_days()
                        elif command == 4:
                            self.__show_events_in_month()
                        elif command == 5:
                            break
                        else:
                            print("Invalid command!")
            except Exception as error:
                print(error)
