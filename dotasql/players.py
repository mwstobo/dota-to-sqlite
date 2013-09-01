import sqlite3
import tools
import abilities

account_id = tools.get_cfg(tools.cfg_filename, "account-id")
conn = sqlite3.connect("matches_{0}".format(account_id))
c = conn.cursor()

def _create_tables():
	c.execute("""
		CREATE TABLE players (
			match_id INTEGER,
			account_id INTEGER,
			player_slot INTEGER,
			hero_id INTEGER,
			item_0 INTEGER,
			item_1 INTEGER,
			item_2 INTEGER,
			item_3 INTEGER,
			item_4 INTEGER,
			item_5 INTEGER,
			kills INTEGER,
			deaths INTEGER,
			assists INTEGER,
			leaver_status INTEGER,
			gold INTEGER,
			last_hits INTEGER,
			denies INTEGER,
			gpm INTEGER,
			xpm INTEGER,	
			gold_spent INTEGER,
			hero_damage INTEGER,
			tower_damage INTEGER,
			hero_healing INTEGER,
			level INTEGER
		)
	""")
	conn.commit()
	
def _check_tables():
	c.execute("""
		SELECT name FROM sqlite_master
		WHERE type='table' AND name LIKE 'players'
	""")
	if c.fetchone() == None:
		_create_tables()
		
def add_player(info, match_id):
	_check_tables()
	if type(info) is not dict:
		raise TypeErorr("Excepted paramater to be dict!")
	account_id = info['account_id']
	player_slot = info['player_slot']
	hero_id = info['hero_id']
	item_0 = info['item_0']
	item_1 = info['item_1']
	item_2 = info['item_2']
	item_3 = info['item_3']
	item_4 = info['item_4']
	item_5 = info['item_5']
	kills = info['kills']
	deaths = info['deaths']
	assists = info['assists']
	leaver_status = info['leaver_status']
	gold = info['gold']
	last_hits = info['last_hits']
	denies = info['denies']
	gpm = info['gold_per_min']
	xpm = info['xp_per_min']
	gold_spent = info['gold_spent']
	hero_damage = info['hero_damage']
	tower_damage = info['tower_damage']
	hero_healing = info['hero_healing']
	level = info['level']
	abilities.add_abilities(info, match_id)
	data = (match_id, account_id, player_slot, hero_id, item_0, item_1, item_2, item_3,
			item_4, item_5, kills, deaths, assists, leaver_status, gold,
			last_hits, denies, gpm, xpm, gold_spent, hero_damage, tower_damage,
			hero_healing, level)
	c.execute("""
		INSERT INTO players VALUES (
			?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
			?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
		)
	""", data)
	conn.commit()
