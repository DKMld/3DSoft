from django import template

register = template.Library()


def sum_two_num(num1, num2):
    value = num1 + num2
    return value


def round_number(num):
    value = round(num)
    return value


register.filter('sum_two_num', sum_two_num)
register.filter('round_num', round_number)