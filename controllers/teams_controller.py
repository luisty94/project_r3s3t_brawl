from flask import Blueprint, Flask, redirect, render_template, request

from models.team import Team
import repositories.team_repository as team_repository

teams_blueprint = Blueprint("teams", __name__)

@teams_blueprint.route("/teams")
def games():
    teams = team_repository.select_all()
    return render_template("teams/index.html", teams=teams)

@teams_blueprint.route("/teams/new")
def new_team():
    return render_template("teams/new.html")