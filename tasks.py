import random


def task_9_14():
    """
    1) 9.14. Дано слово. Вывести на экран его последний символ.

    :return:
    """
    inWord = input('Введите слово: ')
    if inWord != '':
        print(f'Последний символ слова "{inWord}": {inWord[-1]}')
    else:
        print('Слово не введено!')
    return None


def task_9_15():
    """
    2) 9.15. Дано слово. Вывести на экран его k-й символ.

    :return:
    """
    inWord = input('Введите слово: ')
    charNumber = int(input('Ведите k: '))
    if 0 < k < len(inWord):
        print(f'В слове "{inWord}" k-ый ({charNumber}) символ: ')
    else:
        print('Для введённых параметров отстутствует решение.')
    return None


def task_9_16():
    """
    3) 9.16. Дано слово. Определить, одинаковы ли второй и четвертый символы в нем.

    :return:
    """
    inWord = input('Введите слово: ')
    if len(inWord) > 4:
        if inWord[1] == inWord[3]:
            print(f'Второй ({inWord[1]}) и четвертый ({inWord[3]}) символы в слове {inWord} одинаковы')
        else:
            print(f'Второй ({inWord[1]}) и четвертый ({inWord[3]}) символы в слове {inWord} различны')
    else:
        print('Ведённое слово меньше 4 символов. Решение отсуствует.')

    return None


def task_9_24():
    """
    4) 9.24. Из слова яблоко путем "вырезок" и "склеек" его букв получить слова блок и око.

    :return:
    """
    inWord = 'яблоко'
    blok = ''
    oko = ''
    i: int = 1
    while i < len(inWord):
        if 2 <= i <= 5:
            blok += inWord[i-1]
        if 1 <= (len(inWord) - i) <= 3:
            oko += inWord[i]
        i += 1

    print(inWord)
    print(blok, '=', inWord[1:5])
    print(oko, '=', inWord[-1:-4:-1])
    return None


def task_9_38_a():
    """
    5) 9.38.(а) Дано слово из 12 букв. Поменять местами его трети следующим образом:
        а) первую треть слова разместить на месте третьей, вторую треть — на месте первой,
        третью треть — на месте второй;

    :return:
    """
    inWord = ''.join(chr(random.randint(65,122)) for i in range(0,12))
    print(f'Слово: {inWord}')

    part1 = ''
    part2 = ''
    part3 = ''

    i = 0
    while i < len(inWord):
        if i // 4 == 0:
            part1 += inWord[i]
        elif i // 4 == 1:
            part2 += inWord[i]
        elif i // 4 == 2:
            part3 += inWord[i]
        i += 1

    print(f'part1 = {part1}')
    print(f'part2 = {part2}')
    print(f'part3 = {part3}')

    print(f'\nПервую треть слова разместить на месте третьей, вторую треть — на месте первой,\n'
          f'третью треть — на месте второй:\n\t= {part2} - {part1} - {part3}')

    return None


def task_9_41():
    """
    6) 9.41. Дано название футбольного клуба. Напечатать его на экране "столбиком".

    :return:
    """
    inWord = input('Введите название футбольного клуба: ')
    i = 0
    while i < len(inWord):
        print(f'\t{inWord[i]}')
        i += 1
    return None


def task_9_59():
    """
    7) 9.59. Дано предложение. Определить число букв о в нем.

    :return:
    """
    inWord = input('Ведите предложение: ')

    i = 0
    counterO = 0
    while i < len(inWord):
        if inWord[i] == 'o' or inWord[i] == 'О': counterO += 1
        i += 1

    print(f'Количество буквы "о" ("О") в предложении: {counterO}')

    return None


def task_9_76_b():
    """
    8) 9.76.(б) Дано предложение, в котором имеется несколько букв е. Найти:
        б) порядковый номер последней из них.

    :return:
    """
    inWord = input('Введите предложение: ')

    i = 0
    lastIndex = 0
    while i < len(inWord):
        if inWord[i] == 'е' or inWord[i] == 'Е': lastIndex = i
        i += 1

    if lastIndex != 0:
        print(f'Порядковый номер последней буквы "е": {lastIndex}')
    else:
        print('Буква "е" в предложении не встречается.')

    return None


def task_x_01():
    """
    9) x.01. Дана строка, вывести её наоборот.

    :return:
    """
    inString = input('Введите строку: ')
    i = 1
    outString = ''
    while i <= len(inString):
        outString += inString[-i]
        i += 1

    print(f'Результат работы алгоритма: {outString}\n'
          f'Результат работы "среза" inString[::-1]: {inString[::-1]}')
    return None