# @@ LIST

zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"];
# One animal is missing!

if len(zoo_animals) > 3:
  print ("The first animal at the zoo is the " + zoo_animals[0])
  print ("The second animal at the zoo is the " + zoo_animals[1])
  print ("The third animal at the zoo is the " + zoo_animals[2])
  print ("The fourth animal at the zoo is the " + zoo_animals[3])
  print ("----------8<----------")

# Reassign list
zoo_animals[2] = "hyena"
zoo_animals[3] = "cat"
print (zoo_animals)
print ("----------8<----------")

# Append List and show the len of list
suitcase = [] 
suitcase.append("sunglasses")

suitcase.append("clothes")
suitcase.append("shampoo")
suitcase.append("socks")

list_length = len(suitcase)

print ("There are %d items in the suitcase." % (list_length))
print (suitcase)
print ("----------8<----------")

#Sicing List and String
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

# The first and second items (index zero and one)
first = suitcase[0:2]
# Third and fourth items (index two and three)
middle = suitcase[2:4]
# The last two items (index four and five)
last =  suitcase[4:6]

print (first + middle + last)
print ("----------8<----------")

animals = "catdogfrog"
# The first three characters of animals
cat = animals[:3]
# The fourth through sixth characters
dog = animals[3:6]
# From the seventh character to the end
frog = animals[6:]
print (cat + dog + frog)
print ("----------8<----------")

# Maintain List
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")# Use index() to find "duck"
# Your code here!
animals.insert(duck_index, "cobra")
print (animals) # Observe what prints after the insert operation

backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove('dagger')
print (backpack)
print ("----------8<----------")

# For One and All
my_list = [1,9,3,8,5,7]
for number in my_list:
  print (2 * (number))

start_list = [5, 3, 1, 2, 4]
square_list = []

for number in start_list:
  square_list.append(number ** 2)

square_list.sort()
print (square_list)
print ("----------8<----------")


# @@ DICTIONARY
# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106,}

print (residents['Puffin']) # Prints Puffin's room number

print (residents['Sloth'])
print (residents['Burmese Python'])
print ("----------8<----------")


menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print (menu['Chicken Alfredo'])

# Your code here: Add some dish-price pairs to menu!
menu['Spam'] = 2.50
menu['Proxy'] = 3.14
menu['DLP'] = 5

print ("There are " + str(len(menu)) + " items on the menu.")
print (menu)
print ("----------8<----------")

# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

# Your code here!
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']
zoo_animals['Rockhopper Penguin'] = 'ABC'

print (zoo_animals)
print ("----------8<----------")

# Integrate Dictionary and List
inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
# Add a key to inventory called 'pocket', Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
# .sort() the items in the list stored under the 'backpack' key
inventory['backpack'].sort()
#Then .remove('dagger') from the list of items stored under the 'backpack' key
inventory['backpack'].remove('dagger')
# Add 50 to the number stored under the 'gold' key
inventory['gold'] = 550

print (inventory)
print ("----------8<----------")


# Exercise - A day at the supermarket

# BeFOR We Begin
names = ["Adam","Alex","Mariah","Martine","Columbus"]

for x in names:
  print (x)
print ("----------8<----------")

# This is KEY!
webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Baa" : "The sound a goat makes.",
  "Carpet": "Goes on the floor.",
  "Dab": "A small amount."
}

for key in webster:
  print (webster[key])
print ("----------8<----------")

# Control Flow and Looping
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for even in a:
  if even % 2 == 0:
    print (even)
print ("----------8<----------")

# List and Function - Count how many string "fizz" in list.
def fizz_count(x):
  count = 0
  for item in x:
    if item == "fizz":
      count = count +1
  return count

print (fizz_count(["fizz","cat","fizz"]))
print ("----------8<----------")

# String looping
for letter in "STRING":
  print (letter) # will print all letters

word = "This is my book."
for letter in word:
  if letter == "i":
    print (letter) # will print 2 i
print ("----------8<----------")

# Own your store
prices = {
  "banana" : 4,
  "apple"  : 2,
  "orange" : 1.5,
  "pear"   : 3,
}
stock = {
  "banana" : 6,
  "apple"  : 0,
  "orange" : 32,
  "pear"   : 15,
}

for key in prices:
  print (key)
  print ("price: %s" % prices[key])
  print ("stock: %s" % stock[key])

total = 0
for key in prices:
  total = total + (prices[key] * stock[key])
print (total)
print ("----------8<----------")

# Shopping in the market
shopping_list = ["banana", "orange", "apple"]

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}
    
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

def compute_bill(food):
  total = 0
  for item in food:
    if stock[item] > 0:
      total = total + prices[item]
      stock[item] = stock[item] - 1
  return total

print (compute_bill(shopping_list))
print (stock)
print ("-----Check the stock-----")
print (compute_bill(shopping_list))
print (stock)
print ("-----Check the stock-----")
print (compute_bill(shopping_list))
print (stock)
print ("-----Check the stock-----")
print (compute_bill(shopping_list))
print (stock)
print ("-----Check the stock-----")
print (compute_bill(shopping_list))
print (stock)
print ("-----Check the stock-----")
print (compute_bill(shopping_list))
print (stock)
print ("-----Check the stock-----")
print (compute_bill(shopping_list))
print (stock)

