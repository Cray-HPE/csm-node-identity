#!/bin/bash
# Copyright 2019 Cray Inc. All Rights Reserved.

# This script is submitted to sbatch to run the test

echo start job $(date)

srun $RESOURCES/os/node_identity/check_xnid
echo exit $?

echo end job $(date)

