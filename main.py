from dotasql import tools

cfg_filename = "dotasql.cfg"
account_id = tools.get_cfg(cfg_filename, "account-id")

if __name__ == "__main__":
	tools.index_matches(account_id)