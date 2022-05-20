import random


cast_members = ['Carrie Coon', 'Paul Rudd', 'Finn Wolfhard', 'Mckenna Grace', 'Logan Kim' "Celeste O'Connor", 'Bill Murray', 'Dan Aykroyd', 'Ernie Hudson', 'Annie Potts']


def random_quote():
    quotes = [" Back off, man. I'm a scientist.", " He slimed me.", " That's a big Twinkie.", " Print is dead.", " I collect spores, molds and fungus."]
    print(random.choice(quotes))
    

def question1():
    answer1 = input('The movie takes place in what major city?: ')
    while answer1 == 'New York':
        question2()
    else:
        print('Answer again or you will be stuck in this game forever')
        question1()

def question2():
    answer2 = input('In which year did the latest Ghostbusters release?: ')
    while answer2 == str('2022'):
        question3()
    else:
        print('Answer again or you will be stuck in this game forever')
        question1()

def question3():
    answer3 = input('What is the name of the first ghost the girls encounter?:' )
    while answer3 == 'Gertrude':
        question4()
    else:
        print('Answer again or you will be stuck in this game forever')
        question1()

def question4():
    answer4 = input('When we first see the ghost in the library, what is it doing?: ')
    while answer4 == 'Reading':
        question5()
    else:
        print('Answer again or you will be stuck in this game forever')
        question1()

def question5():
    print('Great job.... but you are not quite there yet. Answer the last question to winner of the quiz!')
    answer5 = input('Which of the following is not a Ghostbuster?: Peter, Ray, Lewis or Winston')
    while answer5 == 'Lewis':
        print('Congratualtions you have won!')
        break
    else:
        print('Answer again or you will be stuck in this game forever')

    


question1()