def calculate(operation, int1, int2):
    if operation == "+":
        return int1 + int2
    elif operation == "-":
        return int1 - int2
    elif operation == "x":
        return int1 * int2
    elif operation == "/":
        return int1 / int2
    else:
        raise Exception(f'Unsupported Operation: {operation}')

def tryGetInt():
    try:
        return int(input())
    except:
        raise Exception('Naughty naughty! That was not an integer :-(')


print("Please enter an operation: x, +, -, /")
operation = input()
print("Please enter an integer:")
int1 = tryGetInt()
print("Please enter anotherj integer:")
int2 = tryGetInt()

result = calculate(operation, int1, int2)

print(f'{int1} {operation} {int2} = {result}')