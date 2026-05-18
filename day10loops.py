from countries import countries
from countries_data import countries_data
'''
for hashtag in range(1,8):
    print("#" * hashtag)

for num in range(0,12):
    product = num ** 2
    print(num, "x", num, "=", product)

for country in countries:
    if "land" in country: 
        print(country)
'''

num = len(countries_data)
print(num)

language_counts = {}

for country in countries_data:
    
