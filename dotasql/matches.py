import sqlite3
import logging
import players

conn = sqlite3.connect("matches")
c = conn.cursor()

def _create_tables():
	c.execute("""
		CREATE TABLE matches (
			id INTEGER PRIMARY KEY,
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
			player_0 INTEGER,
			player_1 INTEGER,
			player_2 INTEGER,
			player_3 INTEGER,
			player_4 INTEGER,
			player_128 INTEGER,
			player_129 INTEGER,
			player_130 INTEGER,
			player_131 INTEGER,
			player_132 INTEGER
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
	player_ids	= []
	for player in info['players']:
		player_ids.append(player['account_id'])
		players.add_player(player, id)
	while len(player_ids) < 10:
		player_ids.append(0)
	data = (id, radiant_win, duration, start_time, seq_num, radiant_tower,
			dire_tower, radiant_barracks, dire_barracks, cluster, first_blood,
			lobby_type, human_player_ids, leagueid,	positive_votes,
			negative_votes, game_mode, player_ids[0], player_ids[1],
			player_ids[2], player_ids[3], player_ids[4], player_ids[5],
			player_ids[6], player_ids[7], player_ids[8], player_ids[9])
	c.execute("""
		INSERT INTO matches VALUES (
			?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
			?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
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
