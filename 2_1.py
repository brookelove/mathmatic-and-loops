'''
PSEUDOCODE
1. prompt use for a whole number between 1-7
    a. don't need to validate
    b. make it an integer
2. take the integer and make a mathematic application
    a. ((2 * int(user_input) + 10) / 2) - user_input
    b. print out the the result
3. take the user input and
    a. convert it to three digit number with incrementing digits
                (three is now three hundered and fourty-five)
        i. create a list and append the x into it
        i. use a for looop to create the two next numbers
        iii. append the two to the new list
        ii. then squish the together to create a number
4. add
    a.those three digits together from 3a
    b. print the reult
5. divide STEP 3 by  STEP 4
    a. divide the 3 digit by the sum of STEP 4
    b. print as a float
6. reprint out STEP 5 truncated
    a. import math
    b. math.mod(the result of 5)
    c. take [0] of the resulting tuple
'''
import math
increment_list = []


def mathematics(x):
    # STEP 2
    arithmatic = (((2 * x + 10)/2) - x)
    print("the result of copmpleting the arithmatic equation, (((2 * x + 10)/2) - x) is ", int(arithmatic))
    # STEP 3
    for i in range(x, x + 3):
        increment_list.append(str(i))
    increment_str = ''.join(increment_list)
    print(
        f"The result from joing {x} and incrementing it twice is: ", increment_str)

    # STEP 4
    adding_increment = int(
        increment_list[0]) + int(increment_list[1]) + int(increment_list[2])
    print(
        f"When adding {increment_list[0]}, {increment_list[1]}, and {increment_list[2]}. You will get {adding_increment}")

# STEP 5
    divide_increments = int(increment_str)/adding_increment
    print(
        f"When you divide {increment_str} by {adding_increment} then you will have the result: {divide_increments}")
# STEP 6
    truncated_float = int(divide_increments)
    print(
        f"When getting the rounded down version of {divide_increments} you get {truncated_float}")


user_input = input('Please choose a whole number between 1 - 7: ')
int_input = int(user_input)
mathematics(int_input)
