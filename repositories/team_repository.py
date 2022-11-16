from db.run_sql import run_sql
from models.team import Team
from models.game import Game
from models.pvp import Pvp

def save(team):
    sql = "INSERT INTO teams (name) VALUES (%s) RETURNING id"
    values = [team.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    team.id = id

def select_all():
    teams = []
    sql = "SELECT * FROM teams"
    results = run_sql(sql)
    for result in results:
        team = Team(result["name"], result["id"])
        teams.append(team)
    return teams

def select(id):
    team = None 
    sql = "SELECT * FROM teams WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        team = Team(result["name"], result["id"])
    return team

def delete_all():
    sql = "DELETE FROM teams"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM teams WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(team):
    sql = "UPDATE teams SET name = %s WHERE id = %s"
    values = [team.name, team.id]
    run_sql(sql, values)

def get_played_games(team):
    games = []
    # sql = "SELECT * FROM pvps LEFT JOIN games ON pvps.game_id = game.id WHERE blue_team_id = %s OR red_team_id = %s";
    sql = "SELECT * FROM pvps LEFT JOIN games ON pvps.game_id = games.id WHERE red_team_id = %s AND blue_team_id = %s"
    values = [team.id]
    results = run_sql(sql, values)
    print(results)
    for result in results:
        # Return PVP objects so we can show the name of the match instead of the name of the game being played
        game = Game(result["name"], result["id"])
        games.append(game)
    return games
