# Calculator

# logo
from mod_10d_art import logo

# Add


def add(n1, n2):
    return n1 + n2

# Subtract


def subtract(n1, n2):
    return n1 - n2

# Multiply


def multiply(n1, n2):
    return n1 * n2

# Divide


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)
    con_question = True

    while con_question:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        cal_func = operations[operation_symbol]
        answer = cal_func(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ") == 'y':
            num1 = answer
        else:
            con_question = False
            calculator()


calculator()
