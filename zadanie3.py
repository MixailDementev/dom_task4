# Задайте последовательность цифр.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []


lst = list("47756688399943")
print(lst)

list_count = []
for i in lst:
    count = 0
    for j in lst:
        if j == i:
            count += 1
    list_count.append(count)
print(list_count)

result = []
for i in range(len(list_count)):
    if list_count[i] == 1:
        result.append(lst[i])
print(result)