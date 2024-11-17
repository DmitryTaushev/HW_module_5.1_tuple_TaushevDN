# У вас есть список:
# cinema_genres = ["комедия", "экшн", "пеплум", "триллер", "комедия",
# "пеплум"]
# Вам необходимо:
# преобразовать данный список в множество;
# добавить 2 жанра на ваш выбор (то что вы захотите);
# удалить какой-то из жанров по вашему выбору;
# удалить некий случайный жанр;
# преобразовать множество обратно в список.

cinema_genres = ["комедия", "экшн", "пеплум", "триллер", "комедия","пеплум"]
# преобразовать данный список в множество;
cinema_genres_set = set(cinema_genres)
# добавить 2 жанра на ваш выбор (то что вы захотите);
cinema_genres_set.add("боевик")
print(cinema_genres_set)
# удалить какой-то из жанров по вашему выбору;
cinema_genres_set.remove("комедия")
print(cinema_genres_set)
# удалить некий случайный жанр;
cinema_genres_set.pop()
print(cinema_genres_set)
# преобразовать множество обратно в список.
cinema_genres_list = list(cinema_genres_set)
print(cinema_genres_list)



