'''
1. prompt user to enter astring or a number
2. print the input as...
    a. string
    b. integer 
    c. floating point 
3. What datatypes can be input that will print without any errors?
'''
user_input = input("Please enter a string or an integer: ")
print(str(user_input))
print(int(user_input))
print(float(user_input))

'''
3. What data types can be input that will print without any errors?
    Integers, because they can be rewritten as a string, integer and a float. A float can not be rewritten as a integer so it will produce an error. A string can not be rewritten as an integer. Any types of collections would be an invalid literal because they are read as one inpu and not individual inputs. 
'''
