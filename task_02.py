# У вас есть кортеж из следующих жанров кино:
# cinema_genres = ("Комедия", "Экшн", "Пеплум", "Триллер")
# Вам необходимо:
# заменить жанр Экшн на Боевик
# добавить жанр по вашему выбору между жанрами боевик, и
# пеплум (я выбрал Фэнтези) вы можете выбрать что хотите.
# Результат вывести в консоль
# преобразовать полученный кортеж в строку. Результат вывести в
# консоль
# Вы можете преобразовывать кортежи в другой тип данных или
# записывать их в новые переменные. Результат работы программы
# должен выглядеть следующим образом:

cinema_genres = ("Комедия", "Экшн", "Пеплум", "Триллер")
cinema_genres_list = list(cinema_genres)
cinema_genres_list[1] = 'Боевик'
cinema_genres = tuple(cinema_genres_list)
print(cinema_genres)

cinema_genres_list.insert(2,'Мелодрама')
cinema_genres = tuple(cinema_genres_list)
print(cinema_genres)
print(','.join(cinema_genres))

