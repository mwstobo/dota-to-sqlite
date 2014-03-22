import sqlite3
import logging
import tools
from database import *

db = Database()

def add_abilities(info, match_id):
    if type(info) is not dict:
        raise TypeErorr("Excepted paramater to be dict!")
    values = []
    values.append(match_id)
    values.append(info['account_id'])
    values.append(info['player_slot'])
    ability_ids = []
    ability_times = []
    if 'ability_upgrades' in info:
        for ability in info['ability_upgrades']:
            ability_ids.append(ability['ability'])
            values.append(ability['ability'])
            ability_times.append(ability['time'])
            values.append(ability['time'])
    while len(ability_ids) < 25:
        ability_ids.append(0)
        values.append(0)
    while len(ability_times) < 25:
        ability_times.append(0)
        values.append(-1)
    db.insert("abilities", tuple(values))

def add_player(info, match_id):
    if type(info) is not dict:
        raise TypeErorr("Excepted paramater to be dict!")
    values = []
    values.append(match_id)
    values.append(info['account_id'])
    values.append(info['player_slot'])
    values.append(info['hero_id'])
    values.append(info['item_0'])
    values.append(info['item_1'])
    values.append(info['item_2'])
    values.append(info['item_3'])
    values.append(info['item_4'])
    values.append(info['item_5'])
    values.append(info['kills'])
    values.append(info['deaths'])
    values.append(info['assists'])
    values.append(info['leaver_status'])
    values.append(info['gold'])
    values.append(info['last_hits'])
    values.append(info['denies'])
    values.append(info['gold_per_min'])
    values.append(info['xp_per_min'])
    values.append(info['gold_spent'])
    values.append(info['hero_damage'])
    values.append(info['tower_damage'])
    values.append(info['hero_healing'])
    values.append(info['level'])
    add_abilities(info, match_id)
    db.insert("players", tuple(values))

def add_match(info):
    if type(info) is not dict:
        raise TypeErorr("Excepted paramater to be dict!")
    values = []
    values.append(info['match_id'])
    values.append(int(info['radiant_win']))
    values.append(info['duration'])
    values.append(info['start_time'])
    values.append(info['match_seq_num'])
    values.append(info['tower_status_radiant'])
    values.append(info['tower_status_dire'])
    values.append(info['barracks_status_radiant'])
    values.append(info['barracks_status_dire'])
    values.append(info['cluster'])
    values.append(info['first_blood_time'])
    values.append(info['lobby_type'])
    values.append(info['human_players'])
    values.append(info['leagueid'])
    values.append(info['positive_votes'])
    values.append(info['negative_votes'])
    values.append(info['game_mode'])
    for player in info['players']:
        add_player(player, info['match_id'])
    db.insert("matches", tuple(values))

def indexed(id):
    c = db.db.cursor()
    c.execute("SELECT * FROM matches WHERE id=?", (id,))
    if c.fetchone() == None:
        return False
    else:
        return True
    c.close()
