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
chmod 700 backup.py delete_backup.py clean_backup.py restore_backup.py state.json backup.json backup_api.py
chown backup:backup backup.py delete_backup.py clean_backup.py restore_backup.py state.json backup.json backup_api.py /usr/local/bin/App-backup-python/

# log dir
mkdir /var/log/backup/
chmod 700 /var/log/backup/
chown backup:backup /var/log/backup/ -R

# systemd units
chown backup:backup backup.service backup.timer api.service
chmod 700 backup.service backup.timer api.service
mv backup.service backup.timer api.service /etc/systemd/system/

# fw gro
firewall-cmd --add-port=8080/tcp --permanent
firewall-cmd --reload

systemctl daemon-reload
systemctl enable --now backup.timer api.service
