

print("This is a string")

print(123)

print(123.5)

print(True)
print(False)


print(len("Hello"))


print("hello"[0])                 
print("hello"[1])
print("hello"[2])
print("hello"[3])
print("hello"[4])



print("Hello".upper()) 
print("HELLO".lower()) 
print("                 hello".strip()) 
print("hello".strip("h")) 



print("the quick brown fox".upper()) 
print("THE QUICK brown fox".lower()) 
print("the quick bROWn fox.".capitalize()) 

print("the quick brown fox fox fox".count("fox")) 
print("the quick brown foxfoxfox".count("fox")) 
print("the quick brown fox fox fox".count("fox "))
print("the quick brown fox fox fox".count("Fox ")) 

print("the quick brown fox".find("quick")) 

print("the quick brown fox".replace("fox","frog")) 

print("the quick brown fox          ".strip())  

print("the quick brown fox".strip("the")) 
print("the quick brown fox".strip("brown")) 
print("the quick brown fox".strip("the quick" "fox")) 



my_name = "Klong"       
my_age = 30             
happy = False           



print(my_name)    


my_name="Katherine"
print(my_name)   



print("My name is", my_name)
print("My name is " + my_name)
print("My name is {}".format(my_name))
print(f"MY name is {my_name}")


print(1+2)    



num1 = 1
num2 = 2
print(num1+num2)



num1 = 7
num2 = 2
num1 = 12
print(num1+num2)



num1=7 

num1 +=1 
print(num1) 





num1 = 20
num2 = 40

if num1 < num2:                                   
    print("Num1 is smaller")                      
elif num1 > num2:                                
    print("num1 is bigger")                       
elif num1 == num2:                                
    print("The are the same")                     
else:                                            
    print("Well how did that happen?")      




pin=1234

if pin!=1234:
    print("Your pin is incorrect")
else:
    print("correct pin")


pin=1234
card="mastercard"

if pin==1234 and card=="visa":
    print("card and pin accepted")
elif pin!=1234 and card=="visa":
    print("This is not the correct pin for this card")
elif pin==1234 and card!="visa":
    print("please try your visa card")
else:
    print("Both your pin and your card are wrong")



pin=1234
card="mastercard"

if pin==1234 or card=="visa":
    print("Close enough!")
else:
    print("Both your pin and your card are wrong")



tries=0

pin=1234

if pin==1234 and tries <4:
    print("Success")
elif pin!=1234 and tries <4:
    print("Oh no, try again")
    tries +=1
    print("you have tried {} times".format(tries))
elif tries >=4:
    print("oops")


def cash_withdrawal():
    print("You are withdrawing cash")
    print("That must be nice!")



cash_withdrawal()


def cash_withdraw(amount,accnum):
    print(f"You are withdrawing {amount} from {accnum}")

cash_withdraw(300,12345678) 

cash_withdraw(300,12345678) 
cash_withdraw(600,87654321) 
cash_withdraw(10,11882277) 





tries = 0

def cash_cash(pin,amount):
    
    global tries
    if pin==1234 and tries <3:
        print(f"well done! You can withdraw {amount}")
    elif pin!=1234 and tries <3:
        print("Incorret pin")
        tries +=1
        print(f"You have tried {tries} times")
    else:
        print("Locked out")
    
cash_cash(1233,500)
cash_cash(1433,500)
cash_cash(3333,500)
cash_cash(4433,500)



def add_up(num1,num2):
    return num1+num2

print(add_up(7,3))



def multiply_by_nine_fifths(celsius):  
    return celsius * (9/5)           

def get_fahrenheit(celsius):           
    return multiply_by_nine_fifths(celsius) + 32  

print("The temperature is {}°F".format(get_fahrenheit(15))) 


fav_songs=["Buddy Holly - Weezer",
    "Sleep - My Chemical Romance",
    "15 Step - Radiohead"
]



print(fav_songs)


print(fav_songs[1])



print(fav_songs)



fav_songs[0]="I Miss You - Blink-182"
print(fav_songs)



print(len(fav_songs))


print(len(fav_songs[0]))


fav_songs.append("Army of Me - Bjork")


print(fav_songs)


fav_songs.pop()

fav_websites=[
    "Reddit",
    "Neopets",
    "Wowhead",
    "GrowRPG"
]

fav_websites.remove("GrowRPG")
print(fav_websites)



print(len(fav_websites)) 



fav_websites.reverse()

print(fav_websites)



fav_websites.pop()
print(fav_websites)



fav_websites=[
    "Reddit",
    "Neopets",
    "Wowhead",
    "GrowRPG"
]


fav_websites.sort()
print(fav_websites)



fav_websites.pop()
print(fav_websites)



fav_drinks=["juice", "tea", "water"]

print(fav_drinks[0])
print(fav_drinks[1])
print(fav_drinks[2])



for drink in fav_drinks:
    print(drink)



for i in fav_drinks:
    print(i)


for i in range(10):
    print(i)



for i in range(10):
    print(i)




for i in range(0,10,1):
    print(i)



for i in range(0,10,2):
    print(i)



for i in range(2,10,2):
    print(i)


for i in range (20):
    print("Here's an ice cream")



class_names=["Ash","Anthony","Elmi","Graham","Kat","Markus","Michal D","Michael S","Tom"]

for name in class_names:
    print(f"Thanks for all your hard work in week one, {name}!")
    print("Hope you enjoyed it!")



num = 0                                            

while num < 10:                                      
    num += 1                                         
    print(num)                                       



import random

my_chosen_num = 13                                  

random_number = random.randint(1,50)               

while my_chosen_num != random_number:               
    print(random_number)                           
    random_number = random.randint(1,50)           

print(f"My number, {my_chosen_num}, matched the random number {random_number}!")  