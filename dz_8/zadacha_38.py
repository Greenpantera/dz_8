# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.
# Формат сдачи: pull-request.
import csv
import os
from os.path import exists
from csv import DictReader, DictWriter

#Создание файла
def create_file():
    with open('phone.csv', 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер']) #массив данных. DictWriter - только для csv.
        f_writer.writeheader()

#Получение данных от user
def get_info():
    enter = input("Введите Фамилию, Имя, Номер: ")
    mas_info = enter.split()
    return mas_info

#Запись данных в файл
def write_file(lst):
    with open('phone.csv', 'r', encoding='utf-8', newline='') as data:
        f_reader = DictReader(data) #получение данных из файла(чтение)
        res = list(f_reader) #список словарей
    with open('phone.csv', 'w', encoding='utf-8', newline='') as data:
        obj = {'Фамилия': lst[0], 'Имя': lst[1], 'Номер': lst[2]} #создаем словарь
        res.append(obj) #в список помещаем словарь в существующий список словарей
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер']) #массив данных.  DictWriter - только для csv.
        f_writer.writeheader() #обходит все элемеенты и дозаписывает
        f_writer.writerows(res)

#Чтение данных из файла.
def read_file(file_name):
    with open('phone.csv', encoding='utf-8') as data:
        f_reader = data.read()
        print(f_reader)

#Функция поиска контакта
def find_contact(file_name):
    os.system("cls")
    enter = input("Введине данные контакта для поиска: ")
    res = []
    with open('phone.csv', "r", encoding="UTF-8") as file:
        data = file.readlines()
        for person in data:
            if enter in person:
                res.append(person)
    if len(res) != 0:
        print(res)
    else:
        print(f"Контакт '{enter}' не найден.")

#Функция изменения контакта
def changeContact(file_name):
    with open('phone.csv', 'r', encoding='utf-8', newline='') as file:
        f_reader = DictReader(file)
        res = list(f_reader)

        index = int(input("Введите порядковый номер контакта, который нужно изменить: "))
        print(res[index])
        key = input("Введите ключ контакта, который нужно удалить: ")
        new_value = input("Введите новое значение: ")
        res[index][key] = new_value

    with open('phone.csv', 'w', encoding='utf-8', newline='') as file:
        f_writer = DictWriter(file, fieldnames=f_reader.fieldnames)  # массив данных.  DictWriter - только для csv.
        f_writer.writeheader()  # обходит все элементы и дозаписывает
        f_writer.writerows(res)


#Удаление данных из файла
def delContact(fileName):
    with open('phone.csv', 'r', encoding='utf-8', newline='') as file:
        # Чтение в список словарей
        f_reader = DictReader(file)
        res = list(f_reader)

        index = int(input("Введите порядковый номер контакта, который нужно удалить: "))
        print(res[index])
        res.pop(index)

    with open('phone.csv', 'w', encoding='utf-8', newline='') as file:
        f_writer = DictWriter(file, fieldnames=f_reader.fieldnames)  # массив данных.  DictWriter - только для csv.
        f_writer.writeheader()  # обходит все элементы и дозаписывает
        f_writer.writerows(res)

#Интерфейс главного меню
def drawMainMenu():
    print(" [q] -- Выход")
    print(" [r] -- Чтение")
    print(" [w] -- Запись")
    print(" [f] -- Поиск")
    print(" [c] -- Изменение")
    print(" [d] -- Удаление")


#Файловый менеджер
def main():
    while True:
        drawMainMenu()
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'r':
            if not exists('phone.csv'):
                create_file()
            print(read_file('phone.csv'))
        elif command == 'w':
            if not exists('phone.csv'):
                create_file()
            write_file(get_info())
        elif command == 'f':
            if not exists('phone.csv'):
                create_file()
            find_contact('phone.csv')
        elif command == 'c':
            if not exists('phone.csv'):
                create_file()
            changeContact('phone.csv')
        elif command == 'd':
            if not exists('phone.csv'):
                create_file()
            delContact('phone.csv')

main()
