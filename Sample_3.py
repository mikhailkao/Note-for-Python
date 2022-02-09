# @@ Conditions and Flow Control

# If statement
def using_control_once():
    if 1 == 1:
        return "Success #1"

def using_control_again():
    if 1 > 1:
        return "Success #2"

print (using_control_once())
print (using_control_again())
print ("----------8<----------")

# Else statement
if 8 > 9:
  print ("I don't get printed!")
else:
  print ("I get printed!")
print ("----------8<----------")

# Elif statement
if 8 > 9:
  print ("I don't get printed!")
elif 8 < 9:
  print ("I get printed!")
else:
  print ("I also don't get printed!")
print ("----------8<----------")

def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0
        
print (greater_less_equal_5(4))
print (greater_less_equal_5(5))
print (greater_less_equal_5(6))
print ("----------8<----------")

# Summary
# Complete the if and elif statements!
def grade_converter(grade):
    if grade >= 90:
        return "A"
    elif 80 <= grade < 90:
        return "B"
    elif 70 <= grade < 80:
        return "C"
    elif 65 <= grade < 80:
        return "D"
    else:
        return "F"
      
# This should print an "A"      
print (grade_converter(92))

# This should print a "C"
print (grade_converter(70))

# This should print an "F"
print (grade_converter(61))


# @@ PygLatin

print ('Welcome to the Pig Latin Translator!')

# Start coding here!
#Py2 ONLY -> rawinput
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
  print original
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
  print (new_word)
else:
  print 'empty'






