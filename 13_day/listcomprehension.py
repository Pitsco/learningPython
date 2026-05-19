'''
num = [(i, i * 8) for i in range(11)]
print(num)

#1. 
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
newnumbers = [numbers[i] for i in range(len(numbers)) if numbers[i] > 0]

print(newnumbers)

#2.
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

new_list = [number for i in list_of_lists for number in i]

print(new_list)

#3. 
tuplelist = [(i, i ** 0, i ** 1, i ** 2,i ** 3, i ** 4,i ** 5) for i in range(10)]
print(tuplelist)

#4. 
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

output = [[country.upper(), country[:3].upper(), capital.upper()] for row in countries for country, capital in row]

#5. 
newcountries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

newoutput = [{'country': country.upper(), 'city': capital.upper()} for row in countries for country, capital in row]

print(output)

'''

#6. 
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
newnames = [firstname + " " + lastname for name in names for firstname, lastname in name]

print(newnames)

#7. slope using lambda
linear_function = 'y = ax+b'
yValue = 3
xValue = 2

slope = lambda x,y: y/x

print(slope(yValue, xValue))