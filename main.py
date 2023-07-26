from domain.event import Event
from domain.participant import Participant
from repository.repository import Repository
from service.event_service import EventService
from service.participant_service import ParticipantService
from ui.console import ConsoleUI

import datetime

event_repository = Repository([
    Event("1", "Concert", "Cluj", 100, 100, datetime.datetime.strptime("30-05-2024", '%d-%m-%Y'), datetime.datetime.strptime("31-05-2024", '%d-%m-%Y'), "https://google.com"),
    Event("2", "Festival", "Bucuresti", 200, 200, datetime.datetime.strptime("01-08-2023", '%d-%m-%Y'), datetime.datetime.strptime("03-08-2023", '%d-%m-%Y'), "https://youtube.com"),
    Event("3", "Concert Da", "Cluj", 300, 300, datetime.datetime.strptime("30-08-2023", '%d-%m-%Y'), datetime.datetime.strptime("03-09-2023", '%d-%m-%Y'), "https://youtube.com"),
    Event("4", "Alt Festival", "Bucuresti", 0, 400, datetime.datetime.strptime("30-10-2023", '%d-%m-%Y'), datetime.datetime.strptime("25-12-2023", '%d-%m-%Y'), "https://google.com"),
    ])

participant_repository = Repository([
    Participant("Ana", "ana.jpg", ["1", "2"]),
    Participant("Bogdan", "bogdan.jpg", ["2", "4"]),
    Participant("Cristina", "cristina.jpg", ["3"]),
])

event_service = EventService(event_repository)
participant_service = ParticipantService(event_repository, participant_repository)

ui = ConsoleUI(event_service, participant_service)

ui.run()
