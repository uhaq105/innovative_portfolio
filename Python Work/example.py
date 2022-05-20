# Object Oriented Programming in Python

#    def __init__(self, name, age):
#class Dog:
#        self.name =  name
#        self.age = age

#    def get_name(self):
#        return self.name

#    def get_age(self):
#        return self.age

#d = Dog('Tim', 34)
#print(d.get_name())
#d2 = Dog('Bill', 12)
#print(d2.get_age())


#print('What is your name?')
#name=input()

#if name:
#    print(f'Hello {name}')
#else:
#    print('you did not provide a name')

#bool = False
#if not bool:
#    print(False)
#else:
#    print(True)


# def add_up():
#    num1 = input('What is the first number?')
#    num2 = input('What is the second number?')


#    try:
#        print(f'{num1} + {num2} is {int(num1) + int(num2)}')

#    except:
#        print('Error!')
#        print('*****************')
#        add_up()

#add_up()

light = False

def light_switch():
    global light
    if light:
        print("Whoa! It's bright in here" )
        light = False
    else:
        print("Who turned out the lights")
        light = True

light_switch()
light_switch()

balance = 100

def cash_withdraw(amount):
    global balance
    print(f'Your balance is {balance}')
    print(f'you are withdrawing {amount}')
    balance -= amount
    print(f'your new balance is {balance}')

cash_withdraw(int(input('amount')))
cash_withdraw(20)
cash_withdraw(20)
cash_withdraw(20)

