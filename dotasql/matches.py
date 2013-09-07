import sqlite3
import logging
import tools
import players

account_id = tools.get_cfg(tools.cfg_filename, "account-id")
conn = sqlite3.connect("matches_{0}".format(account_id))
c = conn.cursor()

def _create_tables():
	c.execute("""
		CREATE TABLE matches (
			id INTEGER,
			radiant_win INTEGER,
			duration INTEGER,
			start_time INTEGER,
			seq_num INTEGER,
			radiant_tower INTEGER,
			dire_tower INTEGER,
			radiant_barracks INTEGER,
			dire_barracks INTEGER,
			cluster INTEGER,
			first_blood INTEGER,
			lobby_type INTEGER,
			human_player_ids INTEGER,
			leagueid INTEGER,
			positive_votes INTEGER,
			negative_votes INTEGER,
			game_mode INTEGER,
			PRIMARY KEY(id)
		)
	""")
	conn.commit()

def _check_tables():
	c.execute("""
		SELECT name FROM sqlite_master
		WHERE type='table' AND name LIKE 'matches'
	""")
	if c.fetchone() == None:
		_create_tables()
		
def add_match(info):
	_check_tables()
	if type(info) is not dict:
		raise TypeErorr("Excepted paramater to be dict!")
	id = info['match_id']
	radiant_win = int(info['radiant_win'])
	duration = info['duration']
	start_time = info['start_time']
	seq_num = info['match_seq_num']
	radiant_tower = info['tower_status_radiant']
	dire_tower = info ['tower_status_dire']
	radiant_barracks = info['barracks_status_radiant']
	dire_barracks = info['barracks_status_dire']
	cluster = info['cluster']
	first_blood = info['first_blood_time']
	lobby_type = info['lobby_type']
	human_player_ids = info['human_players']
	leagueid = info['leagueid']
	positive_votes = info['positive_votes']
	negative_votes = info['negative_votes']
	game_mode = info['game_mode']
	for player in info['players']:
		players.add_player(player, id)
	data = (id, radiant_win, duration, start_time, seq_num, radiant_tower,
			dire_tower, radiant_barracks, dire_barracks, cluster, first_blood,
			lobby_type, human_player_ids, leagueid,	positive_votes,
			negative_votes, game_mode)
	c.execute("""
		INSERT INTO matches VALUES (
			?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
			?, ?, ?, ?
		)
	""", data)
	conn.commit()
	
def indexed(id):
	_check_tables()
	c.execute("SELECT * FROM matches WHERE id=?", (id,))
	if c.fetchone() == None:
		return False
	else:
		return True
