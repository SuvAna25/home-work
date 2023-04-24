# Контакты
# Напишите программу, которая запрашивает у пользователя имя контакта и
# номер телефона, добавляет их в словарь и выводит на экран текущий
# словарь контактов. Запрос на добавление идёт бесконечно (но можно
# задать своё условие для завершения программы). Обеспечьте контроль
# ввода: если это имя уже есть в словаре, то выведите соответствующее
# сообщение.

phonebook = dict()
while True:
    print('Текущие контакты на телефоне:')
    if phonebook:
        for name in phonebook:
            print(name, phonebook[name])
    else:
        print('<Пусто>')
    contact = input('Введите имя: ')
    numbers = int(input('Введите номер телефона: '))
    if contact in phonebook:
        print('Ошибка: такое имя уже существует.')
    else:
        phonebook[contact] = numbers
