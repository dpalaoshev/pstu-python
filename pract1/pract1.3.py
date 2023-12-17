import random

random_list = []

for _ in range(10):
    random_element = random.choice([random.randint(1, 100), float(random.randint(1, 100)), str(random.randint(1, 100))])
    random_list.append(random_element)

print("Список: ", random_list)
print("Список без дубликатов: ", list(set(random_list)))