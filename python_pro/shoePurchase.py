#!/bin/python3

from Shoes import Shoes
#run this program later ..10/19/23
low = Shoes('And 1s', 30)
medium = Shoes('Air Force 1s', 120)
high = Shoes('Off Whites', 400)
 
try:
   shoe_budget = float(input('What is your shoe budget? '))
except ValueError:
   exit('Please enter a number')
  
  # go thru the int : 400, 120, 30
  # then go to class shoes
for shoes in [high, medium, low]:
   shoes.buy(shoe_budget)
