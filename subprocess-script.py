#!/usr/bin/env python

import subprocess

svc = "sshd"

check_cmd = ["ps",
             "-C",
             svc]

service_check = subprocess.call(check_cmd)

if service_check == 0:
  print("The service is running.")
else:
  print("The service is not running")
  print("Starting it...")
  try:
    # subprocess.call(["sudo", "systemctl", "start", svc])
    subprocess.check_output(["sudo", "systemctl", "start", svc])
  except subprocess.CalledProcessError as e:
    print("Could not start the service.")
    print(e)
    exit(1)
  subprocess.call(check_cmd)