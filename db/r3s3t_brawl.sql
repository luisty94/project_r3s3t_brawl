DROP TABLE IF EXISTS games;
DROP TABLE IF EXISTS teams;
DROP TABLE IF EXISTS pvps;

CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(225)
);

CREATE TABLE pvps (
    id SERIAL PRIMARY KEY,
    name VARCHAR(225),
    game_id SERIAL NOT NULL REFERENCES games(id),
    red_team_id SERIAL NOT NULL REFERENCES teams(id),
    blue_team_id SERIAL NOT NULL REFERENCES teams(id),
    red_team_score INT,
    blue_team_score INT 
);