#!/bin/sh
#
# Copyright 2018 Cray Inc. All Rights Reserved.
#
# parse /proc/cmdline for nid= and xname=

mkdir -p /etc/cray/

umask 0333
set -- $(cat /proc/cmdline)
for x in "$@"; do
    case "$x" in
        nid=*)
          echo "${x#nid=}" > /etc/cray/nid
          ;;
        xname=*)
          echo "${x#xname=}" > /etc/cray/xname
          ;;
    esac
done

