import random

random_dict1 = {}
random_dict2 = {}

for i in range(10):
    key = f'key{i}'
    random_dict1[key] = random.choice([random.randint(1, 10), float(random.randint(1, 10))])
    random_dict2[key] = random.choice([random.randint(1, 10), float(random.randint(1, 10))])

print("Словарь 1: ", random_dict1)
print("Словарь 2: ", random_dict2)

intersection = set(random_dict1.values()).intersection(set(random_dict2.values()))
print("Пересечение значений:", intersection)

new_dict = {key: value for key, value in random_dict1.items() if value in intersection}
print("Словарь 3:", new_dict)