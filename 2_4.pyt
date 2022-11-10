'''
1. promt for number
2. make into integer
3. print the number 0 if even print number 1 if odd
CANT USE IF STATEMNT
'''
import math


def even_or_odd(x):
    y = (x/2)
    y = math.modf(y)
    return print(f"After inputing {user_input} the computer has deterimed that it will be either even, indicated by 0 or odd represented by a number 1. Here are the reults: {int(y[-1])}")


user_input = input("Please input a number: ")
user_int = int(user_input)
even_or_odd(user_int)
