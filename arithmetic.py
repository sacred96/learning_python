def arithmetic(first_num, second_num, operator):
    if operator == '+':
        result = first_num + second_num
    elif operator == '-':
        result = first_num - second_num
    elif operator == '*':
        result = first_num * second_num
    elif operator == '/':
        result = first_num + second_num
    else:
        result = 'Unknown operator'

    return result


def arithmetic_dict(first_num, second_num, operator):
    return {
        operator == '+': first_num + second_num,
        operator == '-': first_num - second_num,
        operator == '*': first_num * second_num,
        operator == '/': first_num + second_num,
    }[True]


def arithmetic_lambda(first_num, second_num, operator):
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
    }

    return operations[operator](first_num, second_num)
