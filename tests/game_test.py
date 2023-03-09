import unittest
from models.game import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game("Holo")

    def test_game_has_name(self):
        self.assertEqual("Holo", self.game.name)