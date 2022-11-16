from flask import Blueprint, Flask, redirect, render_template, request

from models.game import Game
from models.team import Team
from models.pvp import Pvp
import repositories.pvp_repository as pvp_repository
import repositories.game_repository as game_repository
import repositories.team_repository as team_repository

pvps_blueprint = Blueprint("pvps", __name__)


# INDEX
@pvps_blueprint.route('/pvps')
def pvps():
    pvps = pvp_repository.select_all()
    return render_template('pvps/index.html', all_pvps = pvps)

# NEW

@pvps_blueprint.route('/pvps/new',  methods=['GET'])
def new_pvp():
    games = game_repository.select_all()
    teams = team_repository.select_all()
    return render_template('pvps/new.html', games=games, teams=teams)

# CREATE
# /bitings POST create_biting()
@pvps_blueprint.route('/pvps', methods=["POST"])
def create_pvp():
    name = request.form['name']
    game_id = request.form['game_id']
    team_id = request.form['team_id']
    red_team_id = request.form['team_id']
    blue_team_id = request.form['blue_team_id']
    red_team_score = request.form['red_team_score']
    blue_team_score = request.form['blue_team_score']
    game = game_repository.select(game_id)
    red_team = team_repository.select(team_id)
    blue_team = team_repository.select(team_id)
    new_pvp = Pvp(name, game, red_team, blue_team, red_team_score, blue_team_score)
    pvp_repository.save(new_pvp)
    return redirect('/pvps')

@pvps_blueprint.route("/pvps/<id>/edit")
def edit_pvp(id):
    pvps = pvp_repository.select(id)
    games = game_repository.select_all()
    teams = team_repository.select_all()
    return render_template('pvps/edit.html', pvps=pvps, games=games, teams=teams)

# UPDATE
@pvps_blueprint.route("/pvps/<id>", methods = ["POST"])
def update_pvp(id):
    name = request.form['name']
    game_id = request.form['game_id']
    team_id = request.form['team_id']
    red_team_id = request.form['team_id']
    blue_team_id = request.form['blue_team_id']
    red_team_score = request.form['red_team_score']
    blue_team_score = request.form['blue_team_score']
    game = game_repository.select(game_id)
    red_team = team_repository.select(team_id)
    blue_team = team_repository.select(team_id)
    pvp = Pvp(name, game, red_team, blue_team, red_team_score, blue_team_score)
    pvp_repository.update(pvp)
    return redirect('/pvps')

# DELETE

@pvps_blueprint.route("/pvps/<id>/delete", methods = ["POST"])
def delete_pvp(id):
    pvp_repository.delete(id)
    return redirect("/pvps")
