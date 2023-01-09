#!/usr/bin/env python

import os

# print(os.getcwd())

# os.system('ls')

file = input("Enter a file name: ")

if os.path.isfile(file):
	print("File exists")
else:
	print("File does not exist")
	print("Creating file...")
  os.system('touch {}'.format(file))