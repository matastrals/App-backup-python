#  GNU nano 5.6.1                                           init.sh                                                      #!/bin/bash
# -*- ENCODING: UTF-8 -*-


if [[ $(id -u) -ne 0 ]] ; then
  echo "Déso t pa rout"
  exit 1
fi

# users
groupadd backup
useradd -m -g backup -s /usr/sbin/nologin backup

# app files
chmod 700 backup.py delete_backup.py add_backup.py clean_backup.py restore_backup.py state.json backup.json
chown backup backup.py delete_backup.py add_backup.py clean_backup.py restore_backup.py state.json backup.json

# log dir
mkdir /var/log/backup/
chmod 700 /var/log/backup/
chown backup /var/log/backup/ -R

# systemd units
chown backup backup.service backup.timer
chmod 700 backup.service backup.timer
mv backup.service backup.timer /etc/systemd/system/

systemctl daemon-reload
systemctl enable --now backup.timer
