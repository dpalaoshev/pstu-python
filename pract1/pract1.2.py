import random

list1 = [random.randint(1, 100) for _ in range(10)]
list2 = [random.randint(1, 100) for _ in range(10)]

print("Первый список: ", list1)
print("Второй список: ", list2)

combined_list = []
for i in range(len(list1)):
    if i % 2 == 0:
        combined_list.append(list1[i])
    else:
        combined_list.append(list2[i])

print("Третий список: ", combined_list)
