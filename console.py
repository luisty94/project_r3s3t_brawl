import pdb

from models.game import Game
import repositories.game_repository as game_repository

from models.team import Team
import repositories.team_repository as team_repository

from models.pvp import Pvp
import repositories.pvp_repository as pvp_repository

game_repository.delete_all()
team_repository.delete_all()

team_1 = Team("Queso")
team_repository.save(team_1)

team_2 = Team("Team Liquid")
team_repository.save(team_2)

team_3 = Team("Cloud9")
team_repository.save(team_3)

team_4 = Team("Dignitas")
team_repository.save(team_4)

game_1 = Game("League of Legends")
game_repository.save(game_1)

game_2 = Game("Fortnite")
game_repository.save(game_2)

score_1 = 1
score_2 = 2
score_3 = 3
score_4 = 2

pvp_1 = Pvp("Semifinal", game_1, team_1, team_2, score_1, score_2)
pvp_2 = Pvp("Final", game_1, team_2, team_4, score_3, score_4)
pvp_3 = Pvp("Final2", game_1, team_2, team_4, score_3, score_4)
print ("this is the score")
print (score_2)
pvp_repository.save(pvp_1)
pvp_repository.save(pvp_2)
pvp_repository.save(pvp_3)
pdb.set_trace()
