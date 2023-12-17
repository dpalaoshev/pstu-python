import random

random_dict = {}

for i in range(10):
    key = f'key{i}'
    random_element = random.choice([random.randint(1, 100), float(random.randint(1, 100))])
    random_dict[key] = random_element

unique_values = set(random_dict.values())
random_tuples = []

for value in unique_values:
    keys = [key for key, val in random_dict.items() if val == value]
    random_tuples.append((value, keys))

print("Кортежи: ", random_tuples)
