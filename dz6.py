#Задача 1

# Вариант с циклами
def progression():
    a1, d, n = map(int, input("Укажите через запятую значения параметров арифметической прогрессии - a1, d, n: ").split(','))
    result = []
    result += [a1 + step * d for step in range(n)]
    return result

print(progression())

# Вариант с рекурсией
def progression_rec(a1: int, d: int, n: int) -> list:
    if n == 1:
        return [a1]
    prev_items = progression_rec(a1, d, n-1)
    return prev_items + [a1 + (n-1) * d]

print(progression_rec(7, 2, 5))


#Задача2

lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

def list_in_range(lst1: list, _min: int, _max: int) -> list:
    return [(idx, val) for idx, val in enumerate(lst1) if _min <= val <= _max ]

print(list_in_range(lst1, 2, 10))
