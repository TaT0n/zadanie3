# Реализовать декоратор функции
def func():
    print('Я конфетка')  # возьмем конфетку


def decor(func_to_decor):  # создадим декоратор
    def wrapper():  # поместим в декоратор фантик, бантик, и конфетку
        print('Я бантик')
        print('Я фантик')
        func_to_decor()
        print('Я фантик')

    return wrapper()


decor(func)  # обернем конфетку в фантик и завяжем бантик
