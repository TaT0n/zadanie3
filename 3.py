# Реализовать функцию проверки, является ли введенная фраза полиндромом
word = '123455554321'


def func(word):
    if word == word[-1::-1]:
        print('True')
    else:
        print('False')


func(word)
