count = 0

if count <= 9:
  print ("Hello, I am an if statement and count is", count)

while count <= 9:
  print ("Hello, I am a while and count is", count)
  count += 1
print ("----------8<----------")

num = 1

while num <= 10:
  print (num ** 2)
  num += 1
print ("----------8<----------")

count = 0

while True:
  print (count)
  count += 1
  if count >= 10:
    break
print ("----------8<----------")

import random

print ("Lucky Numbers! 3 numbers will be generated.")
print ("If one of them is a '5', you lose!")

count = 0
while count < 3:
  num = random.randint(1, 6)
  print (num)
  if num == 5:
    print ("Sorry, you lose!")
    break
  count += 1
else:
  print ("You win!")
print ("----------8<----------")

# -----Simple guess game-----
#from random import randint
#
#random_number = randint(1, 10)
#
#guesses_left = 3
#print (random_number)
#while guesses_left > 0:
#  guess = int(input("Your guess: "))
#  if guess == random_number:
#    print ("You win!")
#    break
#  guesses_left -= 1
#else:
#  print ("You lose.")
#  
#print ("----------8<----------")

for i in range(20):
  print (i)
print ("----------8<----------")

# -----Practice of For loop----py2 only
#hobbies = []
#
#for num in range(3):
#  i = input("Input your hobbie: ")
#  hobbies.append(i)
#
#print (hobbies)

thing = "spam!"
for c in thing:
  print (c)

word = "eggs!"
for d in word:
  print (d)
print ("----------8<----------")

# -----Practice-----py2 only
#phrase = "A bird in the hand..."
#
#for char in phrase:
#  if char == "A" or char == "a":
#    print 'X',
#  else:
#    print char,
#
#print

numbers  = [7, 9, 12, 54, 99]

print ("This list contains: ")

for num in numbers:
  print (num)

for num in numbers:
  print (num ** 2)
print ("----------8<----------")

d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
  print (key + " " + d[key])
print ("----------8<----------")

choices = ['pizza', 'pasta', 'salad', 'nachos']

print ('Your choices are:')
for index, item in enumerate(choices):
  print (index+1, item)
print ("----------8<----------")

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
  if a > b:
    print (a)
  else:
    print (b)
print ("----------8<----------")

fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print ('You have...')
for f in fruits:
  if f == 'tomato':
    print ('A tomato is not a fruit!')
    break
  print ('A', f)
else:
  print ('A fine selection of fruits!')
print ("----------8<----------")

# ==========PRACTICE MAKES PERFECT==========
print ('=====PRACTICE MAKES PERFECT=====')

def is_even(x):
  if x % 2 ==0:
    return True
  else:
    return False

def is_int(x):
  if int(x) == x:
    return True
  else:
    return False

def digit_sum(n):
  number = 0
  for a in str(n):
    number += int(a)
  print (number)
  return number

def factorial(x):
  number = 1
  while x > 0:
    number *= x
    x -= 1
  return number

def is_prime(x):
  if x < 2:
    return False
  else: 
    for n in range(2, x-1):
      if x % n == 0:
        return False
    return True

def reverse(text):
  rev = ""
  for i in text:
    rev = i + rev
  return rev

def anti_vowel(text):
  consonant = ""
  for i in text:
    for j in "aeiouAEIOU":
      if i == j:
        i = ""
    consonant = consonant + i
  return consonant


score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
  total_score = 0
  for i in word.lower():
    total_score += score[i]
  return total_score

def censor(text, word): # Must make it clear.
  result = ''
  words = text.split() 
  count = 0
  for i in words:
    if i == word:
      words[count] = '*' * len(word)
    count += 1
  result = ' '.join(words)
  return result

def count(sequence, item):
  ind = 0
  result = 0
  while ind < len(sequence):
    if sequence[ind] == item:
      result += 1
    ind += 1
  return result

def purify(lists):
  new_list = []
  for i in lists:
    if i % 2 == 0:
      new_list.append(i)
  return new_list

def product(lists):
  result = 1
  for i in lists:
    result *= i
  return result  

def remove_duplicates(lists):
  new_list = []
  for i in lists:
    if i not in new_list:
      new_list.append(i)
  return new_list

def median(lists):
  lists.sort()
  count = len(lists) // 2
  if len(lists) % 2 != 0:
    return lists[count]
  else:
    return ((lists[count] + lists[count -  1]) / 2.0) 
