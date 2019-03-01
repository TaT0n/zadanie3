# Реализовать функцию вывода списка с учетом вложенных списков
sp = [1, 'ttt', [1, 2, 3, 'qqq'], [4, 5, 6]]


def func(A):
    print(A)
    for i in range(len(A)):
        if type(A[i]) is int:
            print(A[i], end=' ')
        elif type(A[i]) is str:
            print(A[i], end=' ')
        else:
            for j in range(len(A[i])):
                print(A[i][j], end=' ')


func(sp)
