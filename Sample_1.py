
# Update Variables
money_in_wallet = 40
sandwich_price = 7.50
print (sandwich_price)
sales_tax = .08 * sandwich_price
print (sandwich_price)

 
sandwich_price += sales_tax
print (sandwich_price)

money_in_wallet -= sandwich_price
print (money_in_wallet)

# Two Types of Division

quotient = 7/2
print (quotient)
quotient1 = 7./2
# the value of quotient1 is 3.5
quotient2 = 7/2.
# the value of quotient2 is 3.5
quotient3 = 7./2.
# the value of quotient3 is 3.5

quotient1 = float(7)/2  # Py2 only, no need for Py3
print (quotient1)


# Review and summary...
skill_completed = "Python Syntax"

exercises_completed = 13
#The amount of points for each exercise may change, because points don't exist yet
points_per_exercise = 5


point_total = 100

point_total += exercises_completed * points_per_exercise
print ("I got " + str(point_total) + " points!")