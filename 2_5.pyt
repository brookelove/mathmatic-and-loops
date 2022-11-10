'''
1. constant variable named MAXVAL = 30
2. loop through values 1 - 30
    a. use MAXVAL to determine end of range
3. for each number in the loop 
    a, if it has a porttion that can 
        i.divide evenly into 2 print foo
        ii. divide evenly into 3 print bar
        iii. divide evenly into 5 print baz
    b. print teh output of each number in a loop on a single line



'''
MAXVAL = 30
list_of_words = []


def divide_by_two(x):
    return x % 2


def divide_by_three(x):
    return x % 3


def divide_by_five(x):
    return x % 5


for x in range(MAXVAL+1):
    # print(x)
    if (divide_by_two(x) and divide_by_three(x) and divide_by_five(x) != 0):
        list_of_words.append('')
    if (divide_by_two(x) == 0):
        # append foo to a list
        list_of_words.append("foo")
        # print(f"{x}: foo")
    if (divide_by_three(x) == 0):
        list_of_words.append("bar")
        # print(f"{x}: bar")
    if (divide_by_five(x) == 0):
        list_of_words.append("baz")
        # print(f"{x}: baz")
    joined_list = ''.join(list_of_words)
    print(f"{x}: {joined_list}")
