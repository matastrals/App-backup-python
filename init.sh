#!/bin/bash
# -*- ENCODING: UTF-8 -*-


if [[ $(id -u) -ne 0 ]] ; then
  echo "Déso t pa rout"
  exit 1
fi

# users
groupadd backup
useradd -m -g backup -s /usr/sbin/nologin backup

# app files
chmod 700 backup.py delete_backup.py clean_backup.py restore_backup.py state.json backup.json
chown backup:backup backup.py delete_backup.py clean_backup.py restore_backup.py state.json backup.json /usr/local/bin/App-backup-python/

# log dir
mkdir /var/log/backup/
chmod 700 /var/log/backup/
chown backup:backup /var/log/backup/ -R

# systemd units
chown backup:backup backup.service backup.timer backup_api.py
chmod 700 backup.service backup.timer backup_api.py
mv backup.service backup.timer backup_api.py /etc/systemd/system/

systemctl daemon-reload
systemctl enable --now backup.timer backup_api.py
