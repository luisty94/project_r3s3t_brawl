from db.run_sql import run_sql
from models.pvp import Pvp

from models.game import Game
from models.team import Team
import repositories.game_repository as game_repository
import repositories.team_repository as team_repository
import pdb



def save(pvp):
    sql = "INSERT INTO pvps (name, game_id, red_team_id, blue_team_id, red_team_score, blue_team_score) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    # pdb.set_trace()
    values = [pvp.name, pvp.game.id, pvp.red_team.id, pvp.blue_team.id, pvp.red_team_score, pvp.blue_team_score]
    results = run_sql(sql, values)
    id = results[0]['id']
    pvp.id = id
    return pvp

def select_all():
    pvps = []
    sql = "SELECT * FROM pvps"
    results = run_sql(sql)
    for result in results:
        game = game_repository.select(result['game_id'])
        red_team = team_repository.select(result['team_id'])
        blue_team = team_repository.select(result['team_id'])
        pvp = Pvp(result['name'], game, red_team, blue_team, result['red_team_score'], result['blue_team_score'], result['id'])
        pvps.append(pvp)
    return pvps

# select
def select(id):
    pvp = None
    sql = "SELECT * FROM pvps WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        game = game_repository.select(result['game_id'])
        red_team = team_repository.select(result['team_id'])
        blue_team = team_repository.select(result['team_id'])
        pvp = Pvp(result['name'], game, red_team, blue_team, result['red_team_score'], result['blue_team_score'], result['id'])
    return pvp

# delete
def delete(id):
    sql = "DELETE FROM pvps WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# delete_all
def delete_all():
    sql = "DELETE FROM pvps"
    run_sql(sql)

# update
def update(pvp):
    sql = "UPDATE pvps SET (name, game_id, red_team_id, blue_team_id, red_team_score, blue_team_score) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [pvp.name, pvp.game.id, pvp.red_team.id, pvp.blue_team.id, pvp.red_team_score, pvp.blue_team_score]
    run_sql(sql, values)
