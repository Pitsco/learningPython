from countries_data import countries_data

"""

def arbitrary_named_args(**args):
    print("I received an arbitrary number of arguments, totaling", len(args))
    print("They are provided as a dictionary in my function:", type(args))
    print("Let's print them:")
    for k, v in args.items():
        print(f" * key: {k}, value: {v}")

arbitrary_named_args(name="Derrick", age=30, city="New York")


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(19))

print(36**0.5)


samedata = [1, 2, 3, "three", 4.0, True]

def samedatatype(list):
    for i in range(len(list) - 1):
        if type(list[i]) != type(list[i + 1]):
            return True
        else:
            return False

print(samedatatype(samedata))

def unique(list):
    return len(list) == len(set(list))


def most_spoken_languages(countries_data, top_number):
    language_counts = {}

    for country in countries_data:
        for language in country["languages"]:
            if language in language_counts:
                language_counts[language] += 1
            else:
                language_counts[language] = 1

    sorted_languages = sorted(
        language_counts.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return sorted_languages[:top_number]

print(most_spoken_languages(countries_data, 95))
"""


def most_populated_countries(countries_data, requestednumber):
    sorted_countries = sorted(
        countries_data,
        key=lambda country: country["population"],
        reverse=True
    )

    return sorted_countries[:requestednumber]

ten = most_populated_countries(countries_data, 10)

for i in ten:
    print(i["name"], i["population"])
