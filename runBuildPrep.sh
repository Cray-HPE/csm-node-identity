#!/usr/bin/env bash
# Copyright 2021 Hewlett Packard Enterprise Development LP

# Add zypper repo for cos-buildmacros
if command -v zypper > /dev/null; then
  # Determine what branch we want
  if [[ "$MASTER_BRANCH" == "$PARENT_BRANCH" ]]; then
    REPO_BRANCH="dev/master"
  else
    REPO_BRANCH="$PARENT_BRANCH"
  fi

  zypper ar --no-gpgcheck --refresh http://car.dev.cray.com/artifactory/cos/SHASTA-OS/${TARGET_OS}/noarch/${REPO_BRANCH}/ shasta-os-build-resource
  zypper install -y cos-buildmacros
fi
