# -*- coding: utf-8 -*-
import os
from collections import defaultdict
from random import randint


class GreetingSpeechMaker:
    """
    Use python3.7
    
    Создает поздравления с днем рождения и сохраняет в файл '.txt'.

    Принимает параметры:
    speeches_quantity - (int) количество поздравлений, которое необходимо создать.
    path - (str) путь для сохранения файла с поздравлениями.
    file_name - (str) имя файла с поздравлениями.

    Атрибуты:
    self.files_with_phrase_snippets - хранит названия файлов, содержащих фразы для поздравлений и количество строк в
                                      этих файлах. При инициализации количество строк не задано и добавляется после
                                      запуска метода self.string_counter.

    Методы:
    string_counter - считает количество строк в файлах 'first_part_of_speech.txt' и 'last_part_of_speech.txt'
                     и записывает результат в self.string_quantity_in_files.

    file_reader - случайным образом определяет номер строки с текстом для поздравления и возвращает эту строку.

    make_speech - добавляет в self.text_for_saving строку, возвращенную file_reader.

    save_final_speech - сохраняет текст поздравления в файл на компьютере.

    """

    def __init__(self, speeches_quantity=None, path=None, file_name=None):
        self.speeches_quantity = speeches_quantity if speeches_quantity else 1
        self.file_name = file_name if file_name else 'your_greeting_text.txt'
        if path is None:
            self.path = os.path.join(os.path.dirname(__file__), self.file_name)
        else:
            self.path = os.path.join(os.path.abspath(path), self.file_name)
        self.files_with_phrase_snippets = defaultdict(list)
        self.files_with_phrase_snippets = {
            'first_file': ['first_part_of_speech.txt', ],
            'second_file': ['last_part_of_speech.txt', ]
        }
        self.text_for_saving = []

    def string_counter(self):
        for key, value in self.files_with_phrase_snippets.items():
            _file = self.files_with_phrase_snippets[key][0]
            with open(_file, encoding='utf8') as ff:
                for number, string in enumerate(ff):
                    lines_quantity = number
            value.append(lines_quantity)

    def file_reader(self, key):
        _file = self.files_with_phrase_snippets[key][0]
        with open(file=_file, encoding='utf8') as ff:
            line_number = randint(2, self.files_with_phrase_snippets[key][1])
            for number, line in enumerate(ff):
                if number == line_number:
                    return line[:-1]

    def make_speech(self):
        for key, value in self.files_with_phrase_snippets.items():
            phrase = self.file_reader(key)
            self.text_for_saving.append(phrase)

    def save_final_speech(self):
        final_text = f'С днем рождения!\n{self.text_for_saving[0]}\n{self.text_for_saving[1]}\n\n'
        self.text_for_saving.clear()
        with open(file=self.path, mode='a', encoding='utf8', ) as file:
            file.write(final_text)

    def run(self):
        self.string_counter()
        for _speech in range(self.speeches_quantity):
            self.make_speech()
            self.save_final_speech()
        print(f'Ваше поздравление готово и сохранено в файл "{self.file_name}"!'
              f'\nПолный путь к файлу {self.path}')


if __name__ == '__main__':
    greeting_speech_maker = GreetingSpeechMaker()
    greeting_speech_maker.run()
