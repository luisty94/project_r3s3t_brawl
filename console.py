import pdb

from models.game import Game
import repositories.game_repository as game_repository

from models.team import Team
import repositories.team_repository as team_repository

game_repository.delete_all()
team_repository.delete_all()

game_1 = Game("League of Legends - Day 1 Match")
game_repository.save(game_1)

game_2 = Game("League of Legends - Day 2 Match")
game_repository.save(game_2)

game_3 = Game("League of Legends - Day 3 Match")
game_repository.save(game_2)

game_4 = Game("League of Legends - Day 4 Match")
game_repository.save(game_2)

team_1 = Team("Queso")
team_repository.save(team_1)

team_2 = Team("Team Liquid")
team_repository.save(team_2)

team_3 = Team("Cloud9")
team_repository.save(team_3)

team_4 = Team("Dignitas")
team_repository.save(team_4)

pdb.set_trace()
