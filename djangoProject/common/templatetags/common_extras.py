from django import template

register = template.Library()


def sum_two_num(num1, num2):
    value = num1 + num2
    return value


register.filter('sum_two_num', sum_two_num)