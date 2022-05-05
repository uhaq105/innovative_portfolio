#var1 = 'Welcome to Code Nation'
#print(len(var1))

#var2 = var1

#def isEven():
#    if len(var2) % 2 == 0:
#        print(f'{var2}, The length of the string is {len(var2)} and it is even')
#    else:
#        print('The string is odd -_-')

#print(isEven())

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i','j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for letter in alphabet:
    print(letter)

def letter_num():
    user_num = input('Please enter a number between 1 and 26:     >')
    user_num = int(user_num)
    user_num =-1
    if user_num >=0 and user_num <=26:
        print(alphabet[user_num])
    else:
        print('Invalid entry please try again')
        letter_num()