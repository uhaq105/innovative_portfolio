import random

# print is how we display information in a terminal
print('this is my current file')

# strings are for representing characters
print('Hello my name is Klong')
print('1234')

# This is an integar - a whole number
print(1234)

# This is a floating point - anythin with a decimal
print(1234.5)

# Booleans - True and False
print(True)
print(False)

# None - a blank, or null type
print(None)

# Index position - starts its count at 0
print("hello"[-1])

# Turning strings into upper case letter
print("Hello".upper())

print(random.random())
print(random.uniform(1,10))
print(random.randint(1,10))

import random 
from random import random, randint,uniform

print(uniform())

my_name = 'Klong'
my_age = 30

print(my_name)

print('Hello my name is',my_name)
print('Hello I am '+ my_name)
print('Hello my name is {} and I am {} years old'.format(my_name,my_age))
print(f'Hello my name is {my_name} and I am {my_age} years old')

balance = 100
amount = 50

print(balance=amount)
balance = balance - amount
balance -= amount
print(balance)

char_name = input("What is your name?   >  ")

print(f"Welcome, {char_name}")