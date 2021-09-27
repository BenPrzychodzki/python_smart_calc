from collections import deque

SYMBOLS_PRIORITY = {'(': 0, '+': 1, '-': 1, '−': 1, ')': 1,
                    '*': 2, '/': 2, '%': 2, '^': 3}
OPERATORS = '+−-*/%^'


def conv_to_rpn(equation: str) -> list:
    exit_list = []
    stack = deque()
    for index, symbol in enumerate(equation):
        if symbol.isdigit():
            if index > 0:  # check whether the number has two or more digits. If last symbol in equation was a digit, pop it and add it connected
                if equation[index-1].isdigit():
                    popped_number = exit_list.pop()
                    exit_list.append(popped_number+symbol)
                else:
                    exit_list.append(symbol)
            else:
                exit_list.append(symbol)
        elif symbol == '(':  # if 'open bracket' symbol: add to stack
            stack.append(symbol)
        elif symbol == ')':  # if 'closed bracket' symbol: keep adding to the exit list as long as you reach open bracket symbol
            if stack:
                while stack[-1] != '(':
                    exit_list.append(stack.pop())
                stack.pop()
        elif symbol in OPERATORS:  # if symbol defined in 'OPERATORS' const:
            if symbol in '−-' and len(exit_list) == 0:  # making sure that compute algoritm will make proper calculations
                exit_list.append('0')                   # (e.g. when equation starts with minus sign)
            if len(stack) == 0:  # if stack doesn't have any symbols, add a symbol to it
                stack.append(symbol)
            elif SYMBOLS_PRIORITY[symbol] > SYMBOLS_PRIORITY[stack[-1]]:  # if symbol priority is greater than a priority of top stack symbol, add
                stack.append(symbol)                                      # a symbol to stack
            else:
                while SYMBOLS_PRIORITY[symbol] <= SYMBOLS_PRIORITY[stack[-1]]: # if symbol priority is lesser than a priority of top stack symbol,
                    exit_list.append(stack.pop())                              # keep adding symbols from stack to the exit list as long as their
                    if len(stack) == 0:                                        # priority is greater or equal. After all, add symbol to the stack.
                        break
                stack.append(symbol)                                           
    while len(stack) > 0:
        exit_list.append(stack.pop())
    return exit_list


def symbol_handle(a, b, symbol):
    if symbol == '+':
        return b + a
    elif symbol == '-':
        return b - a
    elif symbol == '*':
        return b * a
    elif symbol == '/':
        return b / a
    elif symbol == '^':
        return b ** a
    elif symbol == '%':
        return b % a
    else:
        return 0


def compute_rpn(rpn_equation: list):
    stack = deque()
    for symbol in rpn_equation:  
        if symbol.isdigit():  # if symbol is digit, put it on a stack
            stack.append(symbol)
        elif symbol in OPERATORS:  # if symbol is an operator, pop two stack items and call symbol handle function, to compute it using given operator
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(symbol_handle(a, b, symbol))
    return stack[-1]