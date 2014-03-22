import os
import sqlite3
import tools

class Database(object):
    def __init__(self):
        account_id = tools.get_cfg(tools.cfg_filename, "account-id")
        db_file = "matches_{0}".format(account_id)
        db_exists = os.path.exists(db_file)
        self.db = sqlite3.connect(db_file)
        if not db_exists:
            self._setup_tables()

    def insert(self, table, values):
        if table == "matches":
            sql = """
                INSERT INTO matches VALUES (
                    ?, ?, ?, ?, ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?, ?, ?, ?
                )
            """
        elif table == "players":
            sql = """
                INSERT INTO players VALUES (
                    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                )
            """
        elif table == "abilities":
            sql = """
                INSERT INTO abilities VALUES (
                    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                )
            """
        else:
            raise ValueError("{0} is not an allowed table!".format(table))
        c = self.db.cursor()
        c.execute(sql, values)
        c.close()
        self.db.commit()

    def _setup_tables(self):
        matches = """
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
                human_players INTEGER,
                leagueid INTEGER,
                positive_votes INTEGER,
                negative_votes INTEGER,
                game_mode INTEGER,
                PRIMARY KEY(id)
            )
        """
        players = """
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
                level INTEGER,
                PRIMARY KEY(match_id, player_slot)
            )
        """
        abilities = """
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
                ability_24_time INTEGER,
                PRIMARY KEY(match_id, player_slot)
            )
        """
        c = self.db.cursor()
        c.execute(matches)
        c.execute(players)
        c.execute(abilities)
        c.close()
        self.db.commit()
