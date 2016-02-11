#!/usr/bin/python

# Function definition is here
def printinfo( name, city, age = 35 ):
   "This prints a passed info into this function"
   print "Name: ", name
   print "Age ", age
   print "City ", city
   return;

# Now you can call printinfo function
printinfo( age=50, name="miki", city='seoul')
printinfo( name="miki", city='seoul' )
# printinfo( name='miki', 'seoul')
printinfo( 'miki', city = 'seoul')
printinfo( 'miki', 'seoul' )