# Activity 1
var1 = 'Welcome to Code Nation'
string_len = len(var1)

def phrase_checker():
    if string_len%2==0:
         print(f"The length of the string \"{var1}\" is {string_len} and it is even")
    else:
        print(f"The length of the string \"{var1}\" is {var1} ")


phrase_checker()

# Activity 2

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for letter in alpha:
    print(letter)


def letter_num():
    user_num=input("please enter a number between 1 and 26:    >")
    user_num=int(user_num)
    user_num -=1
    if user_num >=0 and user_num <=26:
        print(alpha[user_num])
    else:
        print("Invalid entry please try again")
        letter_num()

letter_num()