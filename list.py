numbers = [23,45,37,21,23]

squares = (numb**2 for numb in numbers )
list_of_squares = list(squares)
print(list_of_squares)
# [529, 2025, 1369, 441, 529]

list.append(x)	                      #     Добавляет элемент в конец списка
list.extend(L)	                   #    Расширяет список list, добавляя в конец все элементы списка L
list.insert(i, x)	               #     Вставляет на i-ый элемент значение x
list.remove(x)	                   #    Удаляет первый элемент в списке, имеющий значение x. ValueError, если такого элемента не существует
list.pop([i])	                            #    Удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент
list.index(x, [start [, end]])	          #   Возвращает положение первого элемента со значением x (при этом поиск ведется от start до end)
list.count(x)	                            #    Возвращает количество элементов со значением x
list.sort([key=функция])	            #     Сортирует список на основе функции
list.reverse()	                         #     Разворачивает список
list.copy()	                             #      Поверхностная копия списка
list.clear()	                             #      Очищает список

                         #    ГЕНЕРАТОРЫ СПИСКОВ

a = [a*4 for a in 'Welcome']
#    ['WWWW', 'eeee', 'llll', 'cccc', 'oooo', 'mmmm', 'eeee']

numbers = [numb for numb in range(1,15)]
#    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

c = [a + b for a in "welcome" if a != "e" for b in "Python" if b != "t" and b != "h"]
#    ['wP', 'wy', 'wo', 'wn', 'lP', 'ly', 'lo', 'ln', 'cP', 'cy', 'co', 'cn', 'oP', 'oy', 'oo', 'on', 'mP', 'my', 'mo', 'mn']

