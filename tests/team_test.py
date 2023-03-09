import unittest
from models.team import Team

class TestTeam (unittest.TestCase):

    def setUp(self):
        self.team = Team("Quesote")

    def test_team_has_name(self):
        self.assertEqual("Quesote", self.team.name)