#!/usr/bin/python2.7

import ConfigParser
import pprint
import os


def load_config(config_file):
    conf = ConfigParser.ConfigParser(allow_no_value=True)
    conf.read (config_file)

    # Initialize configuration with default values
    config_info = {
        'mysql.username': 'root',
        'mysql.password': '',
        'mysql.hostname': 'localhost',
        'mysql.port': 3306,
              
        'backup.folder': '/tmp'
	}

    config_info['mysql.username']           = conf.get('mysql', 'username')
    config_info['mysql.password']           = conf.get('mysql', 'password')
    config_info['mysql.hostname']           = conf.get('mysql', 'hostname', 'localhost')
    config_info['mysql.port']               = conf.getint('mysql', 'port')
    config_info['mysql.databases']          = [x.strip() for x in conf.get('mysql', 'databases').split(',')]

    config_info['backup.folder']            = conf.get('backup', 'folder')

    return config_info


filepath = os.path.join (os.path.dirname(os.path.realpath(__file__)), 'backup.conf')
conf = load_config(filepath)


if __name__ == '__main__':
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(conf)