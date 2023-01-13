# ADPY-62
# Домашнее задание к лекции 7.«Подготовка к собеседованию»
# https://github.com/netology-code/py-homeworks-advanced/tree/master/7.Interview

from brackets import Brackets


if __name__ == '__main__':
    brackets = Brackets()
    expressions = ['{([()])}', '{([()]}', '[(ty{ilukl[yuk{iuk utik}iou]*85}oio)iiy]', '{[()])]}', '']
    for expression in expressions:
        is_balanced = brackets.print_is_balanced(expression)

