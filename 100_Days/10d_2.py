# Calculator

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

num1 = int(input("first number?: "))

for symbol in operations:
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = int(input("second number?: "))
    cal_func = operations[operation_symbol]
    answer = cal_func(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")
