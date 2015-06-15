# dbbackup

Installation steps:
1. Unzip the file.
2. Copy backup.conf.template to backup.conf.
3. Edit the values in square brackets.
4. Schedule the backup script in /etc/crontab file to run once every hour. The following line schedules the script to run on the hour every hour.
    0 * * * *       user    /fullpath/main.py
