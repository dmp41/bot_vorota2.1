import csv
import math


with open('prace.csv', encoding='utf-8') as csv_file:
    # считываем содержимое файла
    text = csv_file.readlines()
    # создаем reader объект и указываем в качестве разделителя символ ;
    rows = csv.reader(text, delimiter=',')
    # выводим каждую строку
    rows = list(rows)[1:20]

    long: list[str] = rows[0][1:]  # список значений длин в мм
    hight: {str: str} = {i[0]: i[1:] for i in rows[1:]}  # словарь высота : список цен (находим нужную по индексу длины)


def prace(lg,ht):
    # Округляем числа полученные от пользователя в большую сторону, и преобразуем в строку
    lg=str(math.ceil(int(lg)/100)*100)
    ht=str(math.ceil(int(ht)/100)*100)


    return hight[ht][long.index(lg)]






