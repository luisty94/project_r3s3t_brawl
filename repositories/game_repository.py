from db.run_sql import run_sql
from models.game import Game

def save(game):
    sql = "INSERT INTO games (name) VALUES (%s) RETURNING id"
    values = [game.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    game.id = id

def select_all():
    games = []
    sql = "SELECT * FROM games"
    results = run_sql(sql)
    for result in results:
        game = Game(result["name"], result["id"])
        games.append(game)
    return games

def select(id):
    teaam = None 
    sql = "SELECT * FROM games WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        game = Game(result["name"], result["id"])
    return game

def delete_all():
    sql = "DELETE FROM games"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM games WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(game):
    sql = "UPDATE games SET name = %s WHERE id = %s"
    values = [game.name, game.id]
    run_sql(sql, values)