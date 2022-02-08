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
print ("----------8<----------")

# Data and Time
from datetime import datetime
print (datetime.now())
now = datetime.now()
print (now.year)
print (now.month)
print (now.day)
print (now.hour)
print (now.minute)
print (now.second)
print ('%04d/%02d/%02d %s:%s:%s' % (now.year, now.month, now.day, now.hour, now.minute, now.second))

