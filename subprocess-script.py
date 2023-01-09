#!/usr/bin/env python

import subprocess

svc = "sshd"

service_check = subprocess.call(["ps", "-C", svc])

if service_check == 0:
  print("The service is running.")
else:
  print("The service is not running")