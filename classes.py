#!/usr/bin/env python

class GameCharacter:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def life_check(self):
      if self.health <= 0:
        print(self.name + " was defeated.")
      else:
        print(self.name + " is still alive.")

class Player(GameCharacter):
    def attack(self):
      print(self.name + " kicks the enemy.")

class Enemy(GameCharacter):
    def attack(self):
      print(self.name + " breathes fire!")

    def life_check(self):
      if self.health <= 0:
        print(self.name + " was defeated.")
      else:
        print(self.name + " is still alive.")

def fight(character, target, damage):
  print('\n\n')
  character.attack()
  target.health -= damage
  print(target.name + " has taken " + str(damage) + " damage and has " + str(target.health) + " health left.")
  target.life_check()

player1 = Player("Link", 150)
player2 = Player("Smart", 100)
enemy1 = Enemy("Evil", 150)
enemy2 = Enemy("Shady", 150)

fight(player1, enemy1, 60)
fight(enemy1, player1, 20)
fight(player1, enemy1, 30)
fight(enemy1, player1, 40)
fight(player1, enemy1, 70)
