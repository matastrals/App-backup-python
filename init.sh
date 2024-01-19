#!/bin/bash
# -*- ENCODING: UTF-8 -*-
groupadd backup
useradd -m -d /srv/backup -g backup -s /usr/bin/nologin backup
mkdir /var/log/backup/
chmod 700 /var/log/backup/
chown backup /var/log/backup/ -R backup
chown backup.service
chown backup backup.service
chown backup backup.timer
chmod 700 backup.service
chmod 700 backup.timer
mv backup.service /srv/backup/
mv backup.timer /srv/backup/
systemctl daemon-reload
systemctl start backup.timer
systemctl enable backup.timer
