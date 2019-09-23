#!/bin/bash
#
# Copyright 2019 Cray Inc. All Rights Reserved.
#
# parse /proc/cmdline for nid= and xname=
#
# If this fails, derive xname from IP address

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

# NCNs
# If nid/xname undefined then set xname file based on IP
my_xname()
{
while read n i f a rest; do
  case $i in
    lo|docker*|kube*)
       # skip
       ;;
    *)
      case $f in
        inet6)
          #skip
          ;;
        *)
          # strip trailing mask
          A=${a%%/*}

          # Look for first xname match in hosts entry
          for e in `getent hosts $A`; do
              case $e in
                  x*c*s*b*n*)
                  echo $e
                  return 
                  ;;
              *)
                ;;
              esac
          done
          ;;
      esac
  esac
done < <(ip -o addr)
}

if [ ! -f /etc/cray/xname ]; then
  xname=$(my_xname)
  [ -n "$xname" ] && echo $xname > /etc/cray/xname 
fi
