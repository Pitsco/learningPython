#test
'''
def hello(num):
    if num == 0:
        return "hello"
    if num == 1:
        return "herro"

def world(num):
    if num == 0:
        return "world"
    if num == 0:
        return "galaxy"

def space(num):
    return " "

def highorderfunction(f, num):
    return f"{f(num)}"


print(highorderfunction(hello, 0) + highorderfunction(space, 0) + highorderfunction(world, 0) + highorderfunction(space, 0))

def uppercasedecorator(function):
    def wrapper():
        return function().upper()
    return wrapper

@uppercasedecorator
def helloworld():
    return "HelloWorld!"

print(helloworld())


def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name))

print_full_name("Asabeneh", "Yetayeh",'Finland')

numbers = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x ** 2
print(list(map(square, numbers)))
'''

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#exercises 2:
#1. Use map to create a new list by changing each country to uppercase in the countries list

def uppercase(str):
    return str.upper()

newUpperList = list(map(uppercase, countries))
print(newUpperList)

#2. Use map to create a new list by changing each number to its square in the numbers list
def square(int):
    return int ** 2


newUpperNumsList = list(map(square, numbers))
print(newUpperNumsList)

#3. Use map to change each name to uppercase in the names list
def namesUppercase(str):
    return str.upper()

print(list(map(namesUppercase, names)))

#4. Use filter to filter out countries containing 'land'.
def namesWithLand(str):
    if "land" in str:
        return False
    return True

print(list(filter(namesWithLand, countries)))


#5. Use filter to filter out countries having exactly six characters.
def sixCharacters(str):
    if len(str) == 6:
        return True
    return False

print(list(filter(sixCharacters, countries)))

#6. Use filter to filter out countries containing six letters and more in the country list.

def sixCharactersOrMore(str):
    if len(str) >= 6:
        return True
    return False

print(list(filter(sixCharactersOrMore, countries)))

#7. Use filter to filter out countries starting with an 'E'
def wordswithE(str):
    if "e" in str:
        return True
    return False

print(list(filter(wordswithE, countries)))


#8. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
from functools import reduce

arr = [1, 2, 3, 4, 5, 6, 7]

def double(num):
    return num * 2

def greaterThanTen(num):
    return num > 10

def total(x, y):
    return x + y

print(reduce(total, filter(greaterThanTen, map(double, arr))))

#9. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
listWithStringNum = [1, "two", 3, "four"]
def get_string_lists(item):
    return type(item) == str

print(list(filter(get_string_lists, listWithStringNum)))

#10. Use reduce to sum all the numbers in the numbers list.
def sumOfAll(x,y):
    return x + y

print(reduce(sumOfAll, numbers))

#11. Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
def concatenateCountries(str1, str2):
    return str1 + ", " + str2

print(reduce(concatenateCountries, countries[:-1]) + " and " + countries[-1] + " are north European countries")

#12. Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from countries import countries

def filterout(country):
    if "land" in country or "stan" in country:
        return False
    return True
'''
print(list(filter(filterout, countries)))
'''

#13. Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
from functools import reduce
from countries_data import countries_data

def count_starting_letters(acc, country):
    first_letter = country["name"][0]

    if first_letter in acc:
        acc[first_letter] += 1
    else:
        acc[first_letter] = 1

    return acc

result = reduce(count_starting_letters, countries_data, {})

print(result)

#14. Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
def get_first_ten_countries(countries):
    return [country["name"] for country in countries[:10]]
        
print(get_first_ten_countries(countries_data))

#15. Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries(countries):
    return [country["name"] for country in countries[-10:]]
        
print(get_last_ten_countries(countries_data))

