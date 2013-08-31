import urllib2
import json
import time
import re
import matches

cfg_filename = "dotasql.cfg"

def get_cfg(cfg_filename, cfg_parameter):
	cfg_file = open(cfg_filename, "r").read()
	match = re.search("{0}=(.*)".format(cfg_parameter), cfg_file)
	if match == None:
		raise ValueError("{0} is not in config file.".format(cfg_parameter))
	else:
		return match.group(1)

def gen_match_ids(account_id):
	print "Generating match id's for account {0}...".format(account_id)
	key = get_cfg(cfg_filename, "api-key")
	last_date = time.time()
	remaining, results = 1, 1
	match_ids = []
	while float(remaining) / float(results) != 0:
		url = "https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?key={0}&account_id={1}&date_max={2}".format(key, account_id, last_date)
		u = urllib2.urlopen(url)
		info = json.loads(u.read())
		if info['result']['status'] == 15:
			raise ValueError("No match ids found.")
		remaining = info['result']['results_remaining']
		results = info['result']['num_results']
		last_match_num = info['result']['num_results'] - 1
		last_date = info['result']['matches'][last_match_num]['start_time']
		for match in info['result']['matches']:
			if match_ids.count(match['match_id']) == 0:
				match_ids.append(match['match_id'])
	return match_ids
	
def index_matches(account_id):
	key = get_cfg(cfg_filename, "api-key")
	ids = gen_match_ids(account_id)
	num_added = 0
	num_skipped = 0
	for id in ids:
		if not matches.indexed(id):
			url = "https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/v001/?key={0}&match_id={1}".format(key, id)
			u = urllib2.urlopen(url)
			info = json.loads(u.read())['result']
			matches.add_match(info)
			print "Added match {0}.".format(id)
			num_added += 1
		else:
			print "Skipped match {0} (already indexed).".format(id)
			num_skipped += 1
	print "{0} added. {1} skipped.".format(num_added, num_skipped)
