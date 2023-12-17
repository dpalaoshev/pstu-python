import random

list = [random.randint(1, 100) for _ in range(10)]
print("Список: ", list)

list.reverse()
print("Перевернутый список: ", list)
