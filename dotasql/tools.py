import re

cfg_filename = "dotasql.cfg"

def get_cfg(cfg_filename, cfg_parameter):
    cfg_file = open(cfg_filename, "r").read()
    match = re.search("{0}=(.*)".format(cfg_parameter), cfg_file)
    if match == None:
        raise ValueError("{0} is not in config file.".format(cfg_parameter))
    else:
        return match.group(1)
