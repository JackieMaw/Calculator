def calculateLine(line):
    lineParts = line.split()
    function = lineParts[0]
    operation = lineParts[1]
    int1 = int(lineParts[2])
    int2 = int(lineParts[3])
    return calculate(operation, int1, int2)

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


f = open("C:\Work\Exercises\Calculator\InputPart2.txt")

result = 0
for line in f.read().splitlines():
    result = result + calculateLine(line)

print(f'result = {result}')