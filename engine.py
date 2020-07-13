# -*- coding: utf-8 -*-

from random import randint


def get_first_phrase():
    """
    Берет случайную фразу из файла first_part_of_speech.txt
    """
    lines_quantity = count_lines('first_part_of_speech.txt')
    line_number = randint(2, lines_quantity)
    with open(file='first_part_of_speech.txt', encoding='utf8') as file:
        for number, line in enumerate(file):
            if number == line_number:
                return line


def get_last_phrase():
    """
    Берет случайную фразу из файла last_part_of_speech.txt
    """
    lines_quantity = count_lines('last_part_of_speech.txt')
    line_number = randint(2, lines_quantity)
    with open(file='last_part_of_speech.txt', encoding='utf8') as file:
        for number, line in enumerate(file):
            if number == line_number:
                return line


def count_lines(file_name):
    with open(file_name, mode='r', encoding='utf8') as file:
        for number, line in enumerate(file):
            lines_quantity = number
    return lines_quantity


def get_final_text(first_phrase, last_phrase):
    final_text = f'С днем рождения!\n{first_phrase}\n{last_phrase}'
    file_name = 'your_greeting_text.txt'
    with open(file=file_name, mode='w', encoding='utf8') as file:
        file.write(final_text)
        return print('Ваше поздравление готово и сохранено в файл с названием "your_greeting_text.txt"!')


if __name__ == '__main__':
    first_text_part = get_first_phrase()
    last_text_part = get_last_phrase()
    final_text = get_final_text(first_text_part, last_text_part)
