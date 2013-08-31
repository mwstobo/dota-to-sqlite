Dota to SQLite
================================

A short Python script to access the Dota 2 API, retrieve all of the info for a
specified account id, and store it in a SQLite database file. What you do with
that database is up to you.

Prerequisites
-------------------------
* Python 2.7.*
* (Optional) SQLite command line tool, to verify and explore the database.

Usage
-------------------------
There are three things you need to do in order to use this script:

* Specify your API key in the configuration file, dotasql.cfg. You can get a
Steam API key [here](http://steamcommunity.com/dev/apikey)
* Also in the configuration file, specify the account id you want to index.
The best place to find your proper account id for the API is [DotaBuff]
(http://dotabuff.com). Visit your DotaBuff profile and look at the URL.
The number after "players" is your 32-bit account id.
* From the command line, run `python main.py`. The output will be placed in a
file called matches.

Data structure
-------------------------
The data is structured in three tables: matches, players, and abilities.

**matches**

The matches table holds data specific to each match. Things like match id,
start time, when first blood happened, etc. It also holds a list of account
ids showing which players where a part of the match. If fewer than 10 players
were part of the match, the account id field will be filled with a 0.

**players**

The players table holds data specific to each player. It has information like
account id, hero, kills, items etc. It also holds the match id that the
information was taken from, so each row can be linked back to a specific
match. Note that if a player has the id *4294967295*, it means that they have
not enabled stat tracking in game.

**abilities**

The abilities table holds data on the skill builds in each game. Note that
this feature is relatively new to the API, so not every match will have this
information. This table contains the skill id and time at which it was
skilled. If there is no data on a certain level, the skill id will be 0 and
the time will be -1.
