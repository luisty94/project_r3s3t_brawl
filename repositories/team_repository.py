from db.run_sql import run_sql
from models.team import Team

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
