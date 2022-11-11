'''
PSEUDOCODE
1. prompt user for a umber
2. take the number and cube it then divide by the number
3. print the formula and the reslt 
    a. limit to two decmal places
'''


def cubed_divided_by_num(x):
    y = (x**3)/x
    print(f" The results for the formula is ({x}^3)/{x} = %.2f" % y)


user_input = input("Please enter a number: ")
n = float(user_input)
cubed_divided_by_num(n)
