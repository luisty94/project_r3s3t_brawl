import unittest
from models.game import Game
from models.team import Team
from models.pvp import Pvp

class TestPvp (unittest.TestCase):

    def setUp(self):
        self.team = Team("Quesote")
        self.team2 = Team("Moose")
        self.game = Game("Holo")
        game = self.game
        red_team = self.team
        blue_team = self.team2

        self.pvp = Pvp("Tournament", game, red_team, blue_team, 10, 20)
        
       

    def test_pvp_has_name(self):
        self.assertEqual("Tournament", self.pvp.name)

    def test_pvp_has_game(self):
        self.assertEqual("Holo", self.pvp.game)

    def test_pvp_has_red_team(self):
        self.assertEqual("Quesote", self.pvp.red_team)

    