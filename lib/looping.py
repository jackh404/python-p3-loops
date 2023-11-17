#!/usr/bin/env python3

def happy_new_year():
    i=10
    while i > 0:
        print(i)
        i -= 1
    print('Happy New Year!')

def square_integers(int_list):
    return [num**2 for num in int_list]

def fizzbuzz():
    i=1
    while i < 101:
        if i % 3 and i % 5:
            print(i)
        elif i % 5:
            print('Fizz')
        elif i % 3:
            print('Buzz')
        else:
            print('FizzBuzz')
        i += 1
