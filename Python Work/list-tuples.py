#even_nums = [2, 4, 6, 8, 10]

#odd_nums = [1, 3, 5, 7, 9]
#even_nums.append(12)

#even_nums.insert(5, 0)

#for i in even_nums:
#    print(i)

from this import d


list_of_fruit = [
    'apples',
    'bananas',
    'oranges',
    'pears',
    'grapes',
    'pineapple',
    'star-fruit',
    'mango',
    'cherries',
    'black-berries'
]

nums = [0, 1, 2 ,3 ,4, 5, 6, 7, 8, 9, 10]

num = 0


cofee_tuple = {
    'Usman - mocha',
    'Nick - capuccino'
}

for i in cofee_tuple:
    print(i)

cofee_tuple[0] = 'Usman - Decaf Mocha' # Does not work

for i in cofee_tuple:
    print(i)

list_of_lists = [
    [1, 2, 3],
    [4, 5, 6]
]

print(list_of_lists[1, 0])

even_nums = [2, 4, 6, 8, 10]

odd_nums = (1, 3, 5, 7, 9)

even_nums.append(12)
even_nums.insert(10, 0)

for i in even_nums:
    print(i)


add_nums = odd_nums + (11, 13, 15)

add_nums -= (1,2,3)
print(odd_nums)

list_of_fruit = [
    'apples',
    'bannas',
    'oranges',
    'pears',
    'grapes'
]

print(list_of_fruit[:3])


some_variable = 'djwqj'

while some_variable:
    print('The User has spoken')
    print('Please speak to us!!!')
    if 'orange' in list_of_fruit:
        print('Yay')
        break
    else:
        continue
    print('Please add a fruit')
    fruit = input()
    some_variable = input('Type something')




variable_text = 'This is a text'

example_list = [1, 2, 3, 4, 5, 6, 7]

example_list.append('carrots')

example_list.extend([1, 2, 3, 4])

print(example_list)

example_string = 'fwlfw'

print(len(example_list))

print(type(1001))





class Car():
    color = 'red'
    make = 'Tesla'
    doors = 5
    velocity = 0

    def accelarate():
        velocity += 5

    def stop():
        velocity = 0

wills_car = Car()

wills_car.make = 'VW'
wills_car.color = 'Green'
wills_car.stop()