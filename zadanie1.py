# Вычислить число Пи c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001
# !!! не использовать константу math.pi

# Ряд Лейбница
d = int(input('-> '))
pi = 4 * (sum(1/x for x in range(1, 500000+ 1, 4)) +
            sum(-1/x for x in range(3, 500000 + 1, 4)))
print(round(pi, d))

