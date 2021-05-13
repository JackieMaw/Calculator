def processLine(line, linePointer):

    lineParts = line.split()
    function = lineParts[0]
    result = 0
    linePointer = linePointer + 1

    if function == 'calc':
        operation = lineParts[1]
        int1 = int(lineParts[2])
        int2 = int(lineParts[3])
        print(f'[{linePointer - 1}] calculate {operation} {int1} {int2}')
        result = calculate(operation, int1, int2)
    elif function == 'goto':
        if len(lineParts) == 2:
            print(f'[{linePointer - 1}] goto {lineParts[1]}')
            linePointer = int(lineParts[1])
        elif len(lineParts) == 5:
            operation = lineParts[2]
            int1 = int(lineParts[3])
            int2 = int(lineParts[4])
            print(f'[{linePointer - 1}] goto calculate {operation} {int1} {int2}')
            linePointer = int(calculate(operation, int1, int2))   
        else:
            raise Exception(f'Unsupported goto, should have 2 or 6 parts: "{line}"')

    else:
        raise Exception(f'Unsupported Function: {function}')

    return (result, linePointer)

def calculate(operation, int1, int2):
    if operation == "+":
        return int1 + int2
    elif operation == "-":
        return int1 - int2
    elif operation == "x":
        return int1 * int2
    elif operation == "/":
        return int1 / int2
    elif operation == "^":
        return int1 ^ int2
    else:
        raise Exception(f'Unsupported Operation: {operation}')

def tryGetInt():
    try:
        return int(input())
    except:
        raise Exception('Naughty naughty! That was not an integer :-(')


f = open("C:\Work\Exercises\Calculator\InputPart3.txt")

finalResult = 0
linePointer = -1
nextLinePointer = 0
allLines = f.read().splitlines()
while nextLinePointer != linePointer and nextLinePointer < len(allLines):
    linePointer = nextLinePointer
    (result, nextLinePointer) = processLine(allLines[linePointer], linePointer)
    finalResult += result

print(f'finalResult = {result}')