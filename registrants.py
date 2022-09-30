import requests
import json
import unittest
from unittest import mock
from credentials import token


class RegistrantClass:
    def fetch_registrants(self, baseurl, meetingid):
        url = baseurl + "/meetings/" + meetingid + "/registrants"
        return requests.get(url, headers={'Authorization': 'Bearer ' + token}).json()

    def get_registrant_count(self, baseurl, meetingid):
        registrants = self.fetch_registrants(baseurl, meetingid)
        return str(len(registrants['registrants']))
