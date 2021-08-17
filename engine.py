# -*- coding: utf-8 -*-

import os
import sqlite3
from random import randint

DATABASE = 'phrases.db'


class GreetingSpeechMaker:
    """
    Use python3.7

    Создает поздравления с днем рождения и сохраняет в файл '*.txt'.

    Принимает параметры:
    speeches_quantity - (int) количество поздравлений, которое необходимо создать.
    path - (str) путь для сохранения файла с поздравлениями.
    file_name - (str) имя файла с поздравлениями.

    Методы:
    get_db_row_quantity - считает коилчество записей в БД, возвращает кортеж с количеством записей в первой и второй
                          таблицах БД.

    make_speech - достает из БД строки и добавляет их в self.text_for_saving.

    save_final_speech - сохраняет текст поздравления в файл на компьютере.
    """

    def __init__(self, speeches_quantity=None, path=None, file_name=None):
        self.speeches_quantity = speeches_quantity if speeches_quantity else 1
        self.file_name = file_name if file_name else 'your_greeting_text.txt'
        if path is None:
            self.path = os.path.join(os.path.dirname(__file__), self.file_name)
        else:
            self.path = os.path.join(os.path.abspath(path), self.file_name)
        self.text_for_saving = list()

    def get_db_row_quantity(self) -> tuple:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        try:
            data_from_first_db = cursor.execute('SELECT COUNT(*) FROM first_part_of_speech')
            result_from_first_db = int([el[0] for el in data_from_first_db][0])
            data_from_second_db = cursor.execute('SELECT COUNT(*) FROM second_part_of_speech')
            result_from_second_db = int([el[0] for el in data_from_second_db][0])
            result = tuple([result_from_first_db, result_from_second_db])  # tuple(int, int)
        finally:
            cursor.close()
        return result

    def make_speech(self, first_phrase_number: int, second_phrase_number: int) -> None:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        try:
            # Достаем фразу из первой таблицы БД
            data_from_db = cursor.execute(
                'SELECT text FROM first_part_of_speech WHERE id=?', (first_phrase_number,))
            text = [t[0] for t in data_from_db][0]  # Получаем str
            self.text_for_saving.append(text)
            # Достаем фразу из второй таблицы БД
            data_from_db = cursor.execute(
                'SELECT text FROM second_part_of_speech WHERE id=?', (second_phrase_number,))
            text = [t[0] for t in data_from_db][0]  # Получаем str
            self.text_for_saving.append(text)
        finally:
            cursor.close()

    def save_final_speech(self) -> None:
        final_text = f'С днем рождения!\n{self.text_for_saving[0]}\n{self.text_for_saving[1]}\n\n'
        self.text_for_saving.clear()
        with open(file=self.path, mode='a', encoding='utf8', ) as file:
            file.write(final_text)

    def run(self):
        row_quantity_in_first_db, row_quantity_in_second_db = self.get_db_row_quantity()
        for _speech in range(self.speeches_quantity):
            first_phrase_number = randint(1, row_quantity_in_first_db)
            second_phrase_number = randint(1, row_quantity_in_second_db)
            self.make_speech(first_phrase_number, second_phrase_number)
            self.save_final_speech()
        print(f'Ваше поздравление готово и сохранено в файл "{self.file_name}"!'
              f'\nПолный путь к файлу {self.path}')


if __name__ == '__main__':
    greeting_speech_maker = GreetingSpeechMaker()
    greeting_speech_maker.run()
