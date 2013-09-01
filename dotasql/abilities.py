import sqlite3
import tools

account_id = tools.get_cfg(tools.cfg_filename, "account-id")
conn = sqlite3.connect("matches_{0}".format(account_id))
c = conn.cursor()

def _create_tables():
	c.execute("""
		CREATE TABLE abilities (
			match_id INTEGER,
			account_id INTEGER,
			player_slot INTEGER,
			ability_0 INTEGER,
			ability_0_time INTEGER,
			ability_1 INTEGER,
			ability_1_time INTEGER,
			ability_2 INTEGER,
			ability_2_time INTEGER,
			ability_3 INTEGER,
			ability_3_time INTEGER,
			ability_4 INTEGER,
			ability_4_time INTEGER,
			ability_5 INTEGER,
			ability_5_time INTEGER,
			ability_6 INTEGER,
			ability_6_time INTEGER,
			ability_7 INTEGER,
			ability_7_time INTEGER,
			ability_8 INTEGER,
			ability_8_time INTEGER,
			ability_9 INTEGER,
			ability_9_time INTEGER,
			ability_10 INTEGER,
			ability_10_time INTEGER,
			ability_11 INTEGER,
			ability_11_time INTEGER,
			ability_12 INTEGER,
			ability_12_time INTEGER,
			ability_13 INTEGER,
			ability_13_time INTEGER,
			ability_14 INTEGER,
			ability_14_time INTEGER,
			ability_15 INTEGER,
			ability_15_time INTEGER,
			ability_16 INTEGER,
			ability_16_time INTEGER,
			ability_17 INTEGER,
			ability_17_time INTEGER,
			ability_18 INTEGER,
			ability_18_time INTEGER,
			ability_19 INTEGER,
			ability_19_time INTEGER,
			ability_20 INTEGER,
			ability_20_time INTEGER,
			ability_21 INTEGER,
			ability_21_time INTEGER,
			ability_22 INTEGER,
			ability_22_time INTEGER,
			ability_23 INTEGER,
			ability_23_time INTEGER,
			ability_24 INTEGER,
			ability_24_time INTEGER
		)
	""")
	conn.commit()
	
def _check_tables():
	c.execute("""
		SELECT name FROM sqlite_master
		WHERE type='table' AND name LIKE 'abilities'
	""")
	if c.fetchone() == None:
		_create_tables()
		
def add_abilities(info, match_id):
	_check_tables()
	if type(info) is not dict:
		raise TypeErorr("Excepted paramater to be dict!")
	account_id = info['account_id']
	player_slot = info['player_slot']
	ability_ids = []
	ability_times = []
	if 'ability_upgrades' in info:
		for ability in info['ability_upgrades']:
			ability_ids.append(ability['ability'])
			ability_times.append(ability['time'])
	while len(ability_ids) < 25:
		ability_ids.append(0)
	while len(ability_times) < 25:
		ability_times.append(-1)
	data = (match_id, account_id, player_slot, ability_ids[0],
	ability_times[0], ability_ids[1], ability_times[1], ability_ids[2],
	ability_times[2], ability_ids[3], ability_times[3], ability_ids[4],
	ability_times[4], ability_ids[5], ability_times[5], ability_ids[6],
	ability_times[6], ability_ids[7], ability_times[7], ability_ids[8],
	ability_times[8], ability_ids[9], ability_times[9], ability_ids[10],
	ability_times[10], ability_ids[11], ability_times[11], ability_ids[12],
	ability_times[12], ability_ids[13], ability_times[13], ability_ids[14],
	ability_times[14], ability_ids[15], ability_times[15], ability_ids[16],
	ability_times[16], ability_ids[17], ability_times[17], ability_ids[18],
	ability_times[18], ability_ids[19], ability_times[19], ability_ids[20],
	ability_times[20], ability_ids[21], ability_times[21], ability_ids[22],
	ability_times[22], ability_ids[23], ability_times[23], ability_ids[24],
	ability_times[24])
	c.execute("""
		INSERT INTO abilities VALUES (
			?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
			?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
			?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
			?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
			?
		)
	""", data)
	conn.commit()
