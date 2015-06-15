#!/usr/bin/python2.7

from  config import conf
from datetime import datetime
import subprocess
import glob
import os


def filepath(dbname):
    """Returns the name of the file for a given database and type of dump. """
    time = datetime.now()
    filename = dbname + '_' + time.strftime('%Y%m%d%H%M%S_%W') + '.sql.gz'
    name = os.path.join (conf['backup.folder'], filename)
    return unicode(name)

def backup ():
    """
    Dumps the database to a file.
    """
    option_username = '-u' + conf['mysql.username']
    option_password = '-p' + conf['mysql.password']
    option_hostname = '-h' + conf['mysql.hostname']
    option_port     = '-P' + str(conf['mysql.port'])
    for db in conf['mysql.databases']:
        with open(filepath(db), 'wb') as f:
            dump_process = subprocess.Popen(['mysqldump', option_username, option_password, option_hostname, option_port, db], stdout=subprocess.PIPE)
            zip_process = subprocess.Popen(['gzip'], stdin=dump_process.stdout, stdout=f)
            zip_process.wait()
    # End of backup ()


def main():
    """ Entry point of the script, if invoked from another Python script. """
    backup()


if __name__ == '__main__':
    """ If the requirement is to only backup the database, invoke this script. """
    main()