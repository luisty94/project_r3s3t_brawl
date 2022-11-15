from flask import Blueprint, Flask, redirect, render_template, request

from models.game import Game
import repositories.game_repository as game_repository

games_blueprint = Blueprint("games", __name__)

@games_blueprint.route("/games")
def games():
    games = game_repository.select_all()
    return render_template("games/index.html", games=games)

@games_blueprint.route("/games/new")
def new_game():
    return render_template("games/new.html")

@games_blueprint.route("/games", methods=["POST"])
def create_game():
    name = request.form["name"]
    new_game = Game(name)
    game_repository.save(new_game)
    return redirect("/games")

@games_blueprint.route("/games/<id>/edit")
def edit_game(id):
    game = game_repository.select(id)
    return render_template('games/edit.html', game=game)

@games_blueprint.route("/games/<id>", methods=["POST"])
def update_game(id):
    name = request.form["name"]
    game = Game(name, id)
    game_repository.update(game)
    return redirect("/games")

@games_blueprint.route("/games/<id>/delete", methods=["POST"])
def delete_game(id):
    game_repository.delete(id)
    return redirect("/games")

@games_blueprint.route("/games/<id>")
def show_game(id):
    game = game_repository.select(id)
    return render_template('games/show.html', game = game)
