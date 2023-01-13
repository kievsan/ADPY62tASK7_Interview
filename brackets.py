# ADPY-62
# Домашнее задание к лекции 7.«Подготовка к собеседованию»
# Задание 1. Реализовать класс Stack.
# Задание 2. Используя стек из задания 1, необходимо решить задачу на проверку сбалансированности скобок.


BRACKETS = ['()', '[]', '{}']


class Stack:
    """ Variant of Queue that retrieves most recently added entries first. """

    def __init__(self, maxsize: int = 0):
        self.__queue = []
        self.__maxsize = abs(maxsize)

    @property
    def queue(self):
        return self.__queue

    @queue.setter
    def queue(self, q):
        pass

    @property
    def maxsize(self):
        return self.__maxsize

    @maxsize.setter
    def maxsize(self, m):
        pass

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return not bool(self.size())

    def push(self, item) -> bool:
        if self.maxsize and self.size() == self.maxsize:
            print(f'The item "{item}" is not added: the stack has reached its maximum size {self.size()}!')  # ------
            return False
        self.queue.append(item)
        return True

    def peek(self):
        return self.queue[-1]

    def pop(self):
        if self.is_empty():
            print('Not pop item: the stack is empty!')  # -------------------------------------------------
            return None
        return self.queue.pop(-1)


class Brackets:
    """ Скобки в тексте, проверка на сбалансированность скобок """

    def __init__(self, bracket_pairs=None):
        """ :param bracket_pairs: список возможных парных скобок """
        self.__pairs: list = bracket_pairs if type(bracket_pairs) == 'list' else BRACKETS

    @property
    def pairs(self) -> list:
        return self.__pairs

    @pairs.setter
    def pairs(self, pairs):
        pass

    def get_opened(self):
        """ Список возможных открывающих скобок. """
        return [pair[0] for pair in self.pairs]

    def extract_brackets(self, text: str) -> str:
        """ Извлечь все скобки в строке. """
        return ''.join(symbol for symbol in text.strip() if symbol in ''.join(self.pairs))

    def get_partner(self, bracket: str) -> str:
        """ Парная скобка. """
        for pair in self.pairs:
            if bracket in pair:
                return pair[1] if bracket == pair[0] else pair[0]
        return ''

    def is_balanced(self, text: str) -> bool:
        """
        Проверка на сбалансированность кнопок в тексте/коде/выражении
        :balanced: результат проверки
        :brackets_text: строка из скобок, расположенных в тексте
        :opened_brackets: стек открывающих скобок
        """
        balanced = True
        brackets_text = self.extract_brackets(text.strip())
        brackets_len = len(brackets_text)
        if brackets_len % 2 or not brackets_len:  # print('Нечётное число скобок или их нет!')  # --------------------
            balanced = False
        else:
            opened_brackets = Stack(brackets_len // 2)
            for bracket in brackets_text:
                if bracket in self.get_opened():
                    is_added_into_stack = opened_brackets.push(bracket)
                    # print(bracket, '' if is_added_into_stack else 'не', 'добавлена в стек')  # -------------
                else:
                    if opened_brackets.is_empty():  # print('Стек пуст!')  # ----------------------------
                        balanced = False
                        break
                    taken_from_stack = opened_brackets.pop()  # print(taken_from_stack, 'вынута из стека')  # ---------
                    if taken_from_stack != self.get_partner(bracket):  # print(taken_from_stack, '- в стеке нет пары!')
                        balanced = False
                        break
        return balanced

    def print_is_balanced(self, text: str) -> bool:
        balanced = self.is_balanced(text)
        brackets = self.extract_brackets(text)
        if brackets:
            print(f'Скобки {brackets} в строке "{text}" -',
                  'сбалансированные' if balanced else 'разбалансированные!',
                  '\n')
        else:
            print(f'Скобок в строке "{text}" нет!')
        return balanced
