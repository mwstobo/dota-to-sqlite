from dotasql import net, tools

account_id = tools.get_cfg(tools.cfg_filename, "account-id")

if __name__ == "__main__":
	net.index_matches(account_id)
