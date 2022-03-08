# Removing elements from lists
n = [1, 3, 5]
n.pop(0) # return 1
print (n)

n = [1, 3, 5]
n.remove(1) # return nothing
print (n)

n = [1, 3, 5]
del(n[0]) # retuen nothing
print (n)
print ("----------8<----------")

# More than one argument
m = 5
n = 13

def add_function(x, y):
  return x + y

print (add_function(m, n))
print ("----------8<----------")

# Strings in functions
n = "Hello"

def string_function(s):
  return s+'world'

print (string_function(n))
print ("----------8<----------")

# Passing a list to a function
def list_function(x):
  return x

n = [3, 5, 7]
print (list_function(n))
print ("----------8<----------")

# Using an element from a list in a function
def list_function(x):
  return x[1]

n = [3, 5, 7]
print (list_function(n))
print ("----------8<----------")

# Modifying an element of a list in a function
def list_function(x):
  x[1] = x[1] + 3
  return x

n = [3, 5, 7]
print (list_function(n))
print ("----------8<----------")

# List manipulation in functions
n = [3, 5, 7]
def list_extender(lst):
  lst.append(9)
  return lst

print (list_extender(n))
print ("----------8<----------")

#Printing out a list item by item in a function
n = [3, 5, 7]
def print_list(x):
  for i in range(0, len(x)):
    print (x[i])

print (print_list(n))
print ("----------8<----------")

# Modifying each element in a list in a function
n = [3, 5, 7]

def double_list(x):
  for i in range(0, len(x)):
    x[i] = x[i] * 2
  return (x)

print (double_list(n))
print ("----------8<----------")

# Passing a range into a function
def my_function(x):
  for i in range(0, len(x)):
    x[i] = x[i]
  return x

print (my_function(list(range(3))))
print ("----------8<----------")

# Iterating over a list in a function
n = [3, 5, 7]

def total(numbers):
  result = 0
  for i in numbers:
    result += i
  return result

print (total(n))
print ("----------8<----------")

# Using strings in lists in functions
n = ["Michael", "Lieberman"]

def join_strings(words):
  result = ""
  for i in words:
    result += i
  return result

print (join_strings(n))
print ("----------8<----------")

# Using two lists as two arguments in a function
m = [1, 2, 3]
n = [4, 5, 6]

def join_lists(x,y):
  return x + y

print (join_lists(m, n))
print ("----------8<----------")

# Using a list of lists in a function
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

def flatten(lists):
  results = []
  for i in lists:
    for j in i:
      results.append(j)
  return results

print (flatten(n))																	

print ("--------------------BallteShip---------------------")
# Make a List.
board = []

for i in range(5):
  board.append(['O'] * 5)

print (board)
print ("----------8<----------")

# Custom Print 
board = []

for i in range(5):
  board.append(['O'] * 5)

def print_board(board_in):
  for i in board_in:
    print (i)

print_board(board)
print ("----------8<----------")

# Printing Pretty
board = []

for i in range(5):
  board.append(['O'] * 5)

def print_board(board_in):
  for i in board_in:
    #print " ".join(i) #py2 only
    string1 = " "
    print (string1.join(i))

print_board(board)

# Hide...

from random import randint 

# Add your code below!
def random_row(board_in):
  return randint(0, len(board_in)-1)

def random_col(board_in):
  return randint(0, len(board_in)-1)

#random_row(board)
#random_col(board)

# It's Not Cheating - It's Debugging!
ship_row = random_row(board)
ship_col = random_col(board)

print (ship_row)
print (ship_col)

# ...and Seek! - 
#guess_row = int(raw_input("Guess Row: "))
#guess_col = int(raw_input("Guess Col: "))
guess_row = int(input("Guess Row: "))
guess_col = int(input("Guess Col: "))

# You Win
# Danger, Will Robinson!!
# Bad Aim
# Not Again
##### My own code#####
#if ship_row ==  guess_row and ship_col == guess_col:
#  print ("Congratulations! You sank my battleship!")
#elif guess_row not in range(5) or guess_col not in range(5):
#  print ("Oops, that's not even in the ocean.")
#elif board[ship_row][ship_col] == "X":
#  print ("You guessed that one already.")
#else:
#  print ("You missed my battleship!")
#  board[guess_row][guess_col] = "X"
#print_board(board)
##### Answer code#####
#if guess_row == ship_row and guess_col == ship_col:
#  print ("Congratulations! You sank my battleship!")  
#else:
#  if guess_row not in range(5) or \
#    guess_col not in range(5):
#    print ("Oops, that's not even in the ocean.")
#  elif board[ship_row][ship_col] == "X":
#    print ("You guessed that one already.")
#  else:
#    print ("You missed my battleship!")
#    board[guess_row][guess_col] = "X"
#  print_board(board)

# Play It, Sam - 
# Game Over
# A Real Win
for turn in range(4):
  print ("Turn"), turn + 1
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print ("Congratulations! You sunk my battleship!")
    break
  else:
   if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
     print ("Oops, that's not even in the ocean.")
   elif(board[guess_row][guess_col] == "X"):
     print ("You guessed that one already.")
   else:
     print ("You missed my battleship!")
     board[guess_row][guess_col] = "X"
  if turn == 3:
    print ("Game Over")
  print_board(board)
