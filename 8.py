# Создать список словарей с именем и возрастом. Отсортировать список по возрасту
import operator

list_of_dicts = [{'name': 'Anton', 'age': 10}, \
                 {'name': 'Dima', 'age': 9}, \
                 {'name': 'Sveta', 'age': 8}, \
                 {'name': 'Katya', 'age': 7}, \
                 {'name': 'Pasha', 'age': 6}]
print(list_of_dicts)

list_of_dicts.sort(key=operator.itemgetter('age'), reverse=False)
print(list_of_dicts)
for i in list_of_dicts:
    print(i)
