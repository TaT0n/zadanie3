# Найти медиану чисел в списке
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]


def med(num):
    n = len(num)
    if n < 1:
        return None
    elif n % 2 == 1:  # если нечет
        return sorted(num)[n // 2]
    else:
        return sum(sorted(num)[n // 2 - 1:n // 2 + 1]) / 2


print(med(num))
