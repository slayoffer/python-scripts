#!/usr/bin/env python

myfile = "file1.txt"
try:
  file = open(myfile, "a") # a for append mode, w for write mode, r for read mode
except FileNotFoundError as e:
  print("File not found")
  print(e)
  exit(1)

# for line in file:
#   print(line)

movies = ['The Holy Grail', 'The Life of Brian', 'The Meaning of Life']

for m in movies:
  file.write(m + "\n")
file.close()
