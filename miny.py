def my_name(name):
    print(f'My name is {name}')

my_name('Ali')

def my_food(food, drink):
    print(f'I like to eat {food} and while drinking {drink})

my_food('kabsa', "cola")

number = int(input('pick a number '))

def cube(number):
    return number * number * number

def by_three(number):
    if number % 3 == 0:
        print(cube(number))
    else:
        print('false')
by_three(number)