import json

with open('countries.json', 'r') as file:
    countries = json.load(file)

print(countries)

countries_upper = list(map(lambda country: country.upper(), countries))

print(countries_upper)

countries_with_land = list(filter(lambda country: 'land' in country.lower(), countries))

print(countries_with_land)

countries_six_chars = list(filter(lambda country: len(country) == 6, countries))

print(countries_six_chars)

countries_six_or_more = list(filter(lambda country: len(country) >= 6, countries))

print(countries_six_or_more)

countries_not_starting_with_e = list(filter(lambda country: not country.startswith('E'), countries))

print(countries_not_starting_with_e)

from functools import reduce

all_countries_sentence = reduce(lambda x, y: f"{x}, {y}", countries) + ' are countries in Northern Europe.'

print(all_countries_sentence)

filtered_countries = list(
    filter(lambda country: len(country) >= 6, 
        map(lambda country: country.upper(), 
            list(filter(lambda country: not country.startswith('E'), 
                list(filter(lambda country: 'land' in country.lower(), countries)))))))

print(filtered_countries)

categorize_countries = lambda pattern: lambda countries_list: list(filter(lambda country: any(patt in country.lower() for patt in pattern), countries_list))

common_patterns = ['land', 'ia', 'island', 'stan']
filter_by_pattern = categorize_countries(common_patterns)(countries)

print(filter_by_pattern)

def categorize_countries(pattern):
    def filter_countries(countries_list):
        return list(filter(lambda country: any(patt in country.lower() for patt in pattern), countries_list))
    return filter_countries

filter_by_pattern = categorize_countries(common_patterns)(countries)

print(filter_by_pattern)

with open('countries-data.json', 'r') as file:
    countries_data = json.load(file)

print(countries_data)

sorted_by_name = sorted(countries_data, key=lambda country: country['name'])

print(sorted_by_name)

sorted_by_capital = sorted(countries_data, key=lambda country: country['capital'])

print(sorted_by_capital)

sorted_by_population = sorted(countries_data, key=lambda country: country['population'])

print(sorted_by_population)

from collections import Counter

languages = [language for country in countries_data for language in country['languages']]
language_counter = Counter(languages)

most_common_languages = language_counter.most_common(10)

print(most_common_languages)

sorted_by_population = sorted(countries_data, key=lambda country: country['population'], reverse=True)

print(sorted_by_population[:10])


