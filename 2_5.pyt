'''
1. constant variable named MAXVAL = 30
2. loop through values 1 - 30
    a. use MAXVAL to determine end of range
3. for each number in the loop 
    a, if it has a portion that can 
        i.divide evenly into 2 print foo
        ii. divide evenly into 3 print bar
        iii. divide evenly into 5 print baz
        iv. have to clear the list at the end of the for loop
    b. print teh output of each number in a loop on a single line
4. seprator line 
5. create the same idea but with a while loop 

'''
MAXVAL = 30
list_of_words = []


def divide_by_two(x):
    return x % 2


def divide_by_three(x):
    return x % 3


def divide_by_five(x):
    return x % 5


def for_v_foobarbuz():
    for x in range(1, MAXVAL+1):
        if (divide_by_two(x) == 0):
            # append foo to a list
            list_of_words.append("foo")
        if (divide_by_three(x) == 0):
            list_of_words.append("bar")
        if (divide_by_five(x) == 0):
            list_of_words.append("baz")
        joined_list = ''.join(list_of_words)
        list_of_words.clear()
        print(f"{x}: {joined_list}")


for_v_foobarbuz()
print("==================== seperator =================")
