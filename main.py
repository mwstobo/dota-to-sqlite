from dotasql import net, tools

ACCOUNT_ID = tools.get_cfg("account-id")

if __name__ == "__main__":
    net.index_matches(ACCOUNT_ID)
