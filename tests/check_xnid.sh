#!/bin/bash
# Copyright 2019 Cray Inc. All Rights Reserved.
#

echo '1..4'     # expect 4 TAP results
notok=0
if [[ -f /etc/cray/nid ]]; then
    echo ok 1 - /etc/cray/nid exists
else
    echo not ok 1 - /etc/cray/nid does not exist
    notok=1
fi
if [[ -f /etc/cray/xname ]]; then
    echo ok 2 - /etc/cray/xname exists
else
    echo not ok 2 - /etc/cray/xname does not exist
    notok=1
fi

echo ---------- /proc/cmdline
cat /proc/cmdline
echo ---------- /proc/cmdline

clnid=$(tr ' ' '\n' < /proc/cmdline | grep nid | cut -f 2 -d "=")
clxname=$(tr ' ' '\n' < /proc/cmdline | grep xname | cut -f 2 -d "=")
nid=$(</etc/cray/nid)
xname=$(</etc/cray/xname)

if [[ $clnid == $nid ]]; then
    echo ok 3 - /etc/cray/nid matches the commandline
else
    echo not ok 3 - /etc/cray/nid '(' $clnid ')' does not match the commandline
    notok=1
fi
if [[ $clxname == $xname ]]; then
    echo ok 4 - /etc/cray/xname matches the commandline
else
    echo not ok 4 - /etc/cray/xname '(' $clxname ')' does not match the commandline
    notok=1
fi

if [[ notok -eq 0 ]]; then
    echo PASS
else
    echo FAIL
fi
echo EXIT $notok    # this result needs to be passed back to the job wrapper
exit $notok
