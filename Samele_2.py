# Escaping characters
print ('There\'s a snake in my boot!')
print ("----------8<----------")

# Index
T = "PYTHON"[2]
print (T)
print ("----------8<----------")

#String methods
a = "I Love You!"
b = 123
print (len(a))
print (a.lower())
print (a.upper())
print (type(b))
b = str(b)
print (str(b))
print (type(b))
print ("----------8<----------")

# String Formatting [%]
name = "Mike"
print ("Hello %s" % (name))

day = 6
month = 1
year = 2022
print ("%s - %s - %s" %(day, month, year))
print ("%02d - %02d - %s" %(day, month, year))