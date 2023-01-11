#!/usr/bin/env python

foods = ('pizza', 'falafel', 'carrot cake')

try:
  foods[1] = "Macaroni"
except:
  print("An error occurred")