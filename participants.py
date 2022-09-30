import requests
import json
import unittest
from unittest import mock
from credentials import token


class ParticipantClass:
    def fetch_participants(self, baseurl, meetingid):
        url = baseurl + "/metrics/meetings/" + meetingid + "/participants"
        return requests.get(url, headers={'Authorization': 'Bearer ' + token}).json()

    def get_participant_count(self, baseurl, meetingid):
        participants = self.fetch_participants(baseurl, meetingid)
        return str(len(participants['participants']))
