#!/bin/bash
# -*- ENCODING: UTF-8 -*-


if [[ $(id -u) -ne 0 ]] ; then
  echo "Déso t pa rout"
  exit 1
fi

# Pip install
dnf install pip

# Libs python install
pip install paramiko
pip install flask