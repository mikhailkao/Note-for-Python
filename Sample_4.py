# Calculate the price with tax and tips.
def tax(bill):
  """Adds 8% tax to a restaurant bill."""
  bill *= 1.08
  print ("With tax: %f" % bill)
  return bill

def tip(bill):
  """Adds 15% tip to a restaurant bill."""
  bill *= 1.15
  print ("With tip: %f" % bill)
  return bill

# Code for Py2
meal_cost = raw_input("Enter your cost: ")
meal_with_tax = tax(int(meal_cost))
meal_with_tip = tip(int(meal_with_tax))

# Code for Py3
#meal_cost = input("Enter your cost: ")
#meal_with_tax = tax(int(meal_cost))
#meal_with_tip = tip(int(meal_with_tax))
print ("----------8<----------")

# Function Junction
def spam():
  """Print [Eggs!] string."""
  print ("Eggs!")

spam()
print ("----------8<----------")

# Functions Calling Functions
def one_good_turn(n):
  return n + 1
    
def deserves_another(n):
  return one_good_turn(n) + 2

# Function Practice
def cube(number):
  number = number ** 3
  return number

def by_three(number):
  if number % 3 == 0:
    return cube(number)
  else:
    return False

print (cube(2)) # Return 8
print (by_three(3)) #Return 27
print (by_three(1)) #Return False 
print ("----------8<----------")

# General Import
import math
print (math.sqrt(25))

# Function Import
from math import sqrt
print (sqrt(25))

# Universal Imports
from math import *
print (sqrt(25))

# List functions in module
import math
print (dir(math))


# Review Functions
def shut_down(s):
  if s == 'yes':
    return "Shutting down"
  elif s == 'no':
    return "Shutdown aborted"
  else:
    return "Sorry"

print (shut_down('yes'))
print (shut_down('no'))
print (shut_down('miao'))

# Review Modules
import math
print (math.sqrt(13689))

# Review: Built-In Functions
def distance_from_zero(number):
  if type(number) == int or type(number) == float:
    return abs(number)
  else:
    return "Nope"

print (distance_from_zero(-3.14))
print (distance_from_zero('-3.14'))

# Summary - Taking a vacation
def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475
  else:
    return 0

def rental_car_cost(days):
  cost = 40 * days
  if days >= 7:
    cost -= 50
    return cost
  elif days >= 3:
    cost -= 20
    return cost
  else:
    return cost
    
def trip_cost(city, days, spending_money):
  return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money

print (trip_cost("Los Angeles", 5, 600))