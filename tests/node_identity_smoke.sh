#!/bin/bash -e
# Copyright 2019 Cray Inc. All Rights Reserved.
#
# This script is run on the UAI. It's job is to launch the app from
# the resources directory, collect the output, and judge pass/fail.
#
# sbatch is being used at this time due to CASMUSER-969

if [ "$RESOURCES" == "" ]; then
    echo "Expected \$RESOURCES to point to the test resource directory on a shared file system!"
        exit 1
    fi

# create a temporary directory to work in
# $RESOURCES is set by the CT driver to a directory on lustre where the UAI /
# compute tests have been copied to. Creating temporary directories under
# there is permitted.
tmp=$(mktemp -d -p $RESOURCES)
cd $tmp || exit 2
ec=2

sbatch -n 1 --output=job.out --wait $RESOURCES/os/node_identity/compute_job
rc=$?
echo sbatch exit $ec
if [[ $rc -ne 0 ]]; then
    echo FAIL - sbatch exited non-zero $rc
    ec=1
fi
echo ----------
cat job.out
echo ----------

# Look in the job output file to determine the exit code to use, as sbatch
# apparently doesn't pass back the job script's exit code
e=$(grep EXIT job.out | cut -f 2 -d " ")

if [[ -z "$e" ]];then
    echo FAIL - exit code was not found
    ec=1
else
    echo exit code $e
    ec=$e
fi

# clean up temporary directory before exiting
cd /tmp
rm -rf $tmp
exit $ec
