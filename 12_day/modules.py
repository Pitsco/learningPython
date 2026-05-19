from math import *
from math import pi as PI
from random import random, randint
import string 

import random
'''
print(sqrt(pi))

#rename function: from math import pi as PI
print(sqrt(PI))

print(randint(9,10))

#1. 
def random_user_id(len):
    random_string = ""
    characters = string.ascii_letters + string.digits
    for i in range(len):
        random_string += random.choice(characters)
    return random_string


print(random_user_id())


#2: 
def user_id_gen_by_user(numOfChar, numOfIDs):
    for i in range(numOfIDs):
        print(random_user_id(numOfChar))


print(user_id_gen_by_user(5, 5))

#3:
def rgb_color_gen():
    return(randint(0,256), randint(0,256), randint(0,256))

print(rgb_color_gen())


#4:
def list_of_hexa_colors(num):
    for i in range(num):
        hex_value = ""
        for j in range(6):
            hex_value += random.choice(string.hexdigits)
        print("#" + hex_value.upper())
list_of_hexa_colors(5)

#5:
def num_of_hexa(num):
    list = []
    for i in range(num):
        hexavalue = ""
        for i in range(6):
            hexavalue += random.choice(string.hexdigits)
        list.append(hexavalue.upper())
    return list

print(num_of_hexa(5))

#6:

userinput = input("Hexa or RGB: ").lower()

def hexaOrRGB(userinput, num):
    list=[]
    if userinput == 'hexa':

        for i in range(num):
            hexavalue = ""
            for i in range(6):
                hexavalue += random.choice(string.hexdigits)
            list.append(hexavalue.upper())
        return list
    elif userinput == 'rgb':
        for i in range(num):
            list.append(f"rgb({randint(0, 255)}, {randint(0, 255)}, {randint(0, 255)})")
        return list
    else:
        return "Please give a valid input"

print(hexaOrRGB(userinput, 5))
'''

#7: 
def shuffle_list(list):
    random.shuffle(list)
    return list

testlist = [1,2,3,4,5]
print(shuffle_list(testlist))

#8.
def function():
    list = []
    for i in range(7):
        newdigit = randint(0,9)
        if newdigit not in list:
            list.append(newdigit)
    return list
print(function())


