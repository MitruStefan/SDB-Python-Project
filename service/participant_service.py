from domain.event import Event
from domain.participant import Participant
from repository.repository import Repository


class ParticipantService:
    def __init__(self, event_repository: Repository, participant_repository: Repository):
        """
        Constructor for ParticipantService class
        :param repository: participant repository (Repository)
        :return:
        """
        self.__event_repository = event_repository
        self.__participant_repository = participant_repository

    def get_event_participants(self, id):
        """
        Gets the participants for a given event
        :param id: id of the event (string)
        :return: the participants for a given event (list)
        """
        participant_list = self.__participant_repository.get_all()
        event_participants = []
        for participant in participant_list:
            if participant.is_enlisted(Event(id, 0, 0, 0, 0, 0, 0, 0)):
                event_participants.append(participant)

        return event_participants

    def enlist_to_event(self, id, name, profile_picture):
        """
        Enlists a participant to an event
        :param id: id of the event (string)
        :param name: name of the participant (string)
        :param profile_picture: the url of the profile picture of the participant (string)
        :return:
        """
        event = self.__event_repository.find(Event(id, 0, 0, 0, 0, 0, 0, 0))

        if event is None:
            raise Exception("Event does not exist!")
        if event.get_slots() == event.get_participants():
            raise Exception("Event is full!")

        event.set_participants(event.get_participants() + 1)

        participant = Participant(name, profile_picture, [id])
        self.__participant_repository.add(participant)