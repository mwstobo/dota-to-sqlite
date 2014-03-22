import urllib2
import json
import time
import dotasql.tools
import dotasql.matches

def gen_match_ids(account_id):
    print "Generating match ids for account {0}...".format(account_id)
    key = dotasql.tools.get_cfg("api-key")
    last_match_id = ""
    remaining, results = 1, 1
    match_ids = []
    while float(remaining) / float(results) != 0:
        url = "https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?key={0}&account_id={1}&start_at_match_id={2}".format(key, account_id, last_match_id)
        u = urllib2.urlopen(url)
        info = json.loads(u.read())
        if info['result']['status'] == 15:
            raise ValueError("No match ids found.")
        remaining = info['result']['results_remaining']
        results = info['result']['num_results']
        last_match_num = info['result']['num_results'] - 1
        last_match_id = info['result']['matches'][last_match_num]['match_id']
        for match in info['result']['matches']:
            if match_ids.count(match['match_id']) == 0:
                match_ids.append(match['match_id'])
    return match_ids

def index_matches(account_id):
    key = dotasql.tools.get_cfg("api-key")
    ids = gen_match_ids(account_id)
    num_added = 0
    num_skipped = 0
    for match_id in ids:
        if not dotasql.matches.indexed(match_id):
            url = "https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/v001/?key={0}&match_id={1}".format(key, match_id)
            u = urllib2.urlopen(url)
            info = json.loads(u.read())['result']
            dotasql.matches.add_match(info)
            print "Added match {0}.".format(match_id)
            num_added += 1
        else:
            print "Skipped match {0} (already indexed).".format(match_id)
            num_skipped += 1
    print "{0} added. {1} skipped.".format(num_added, num_skipped)
