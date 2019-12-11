def getIntArray(input):
    return [int(i) for i in input.split(",")]


infile = open('day5_input.txt', 'r')

content = getIntArray(infile.readline().strip())
# content = [x.strip() for x in content]

# print(content)

# test = getIntArray("3,0,4,0,99")
# print(test)
# test2 = getIntArray("1002,4,3,4,33")
# print(test2)

output = []

def performStep(startIndex, input):
    instruction = str(input[startIndex]).zfill(5)

    mode1 = int(instruction[2])
    mode2 = int(instruction[1])
    mode3 = int(instruction[0]) 

    value = int(instruction[3:])

    if value == 1:
        firstIndex = input[startIndex + 1]
        secondIndex = input[startIndex + 2]
        thirdIndex = input[startIndex + 3]
        firstValue = input[firstIndex] if mode1 == 0 else firstIndex
        secondValue = input[secondIndex] if mode2 == 0 else secondIndex
        input[thirdIndex] = firstValue + secondValue
        return performStep(startIndex + 4, input)
    elif value == 2:
        firstIndex = input[startIndex + 1]
        secondIndex = input[startIndex + 2]
        thirdIndex = input[startIndex + 3]
        firstValue = input[firstIndex] if mode1 == 0 else firstIndex
        secondValue = input[secondIndex] if mode2 == 0 else secondIndex
        input[thirdIndex] = firstValue * secondValue
        print("Value 2. First Value: " + str(firstValue) + " Second Value: " + str(secondValue))
        return performStep(startIndex + 4, input)
    elif value == 3:
        firstIndex = input[startIndex + 1]
        # User input of 1
        input[firstIndex] = 1
        return performStep(startIndex + 2, input)
    elif value == 4:
        firstIndex = input[startIndex + 1]
        output.append(input[firstIndex])
        return performStep(startIndex + 2, input)
    elif value == 99:
        return 0
    else:
        print("Unknown optcode: " + str(value))
        return 1

def runProgram(input):
    result = performStep(0, input)
    if result == 0:
        return output
    else:
        return None
    # print("Value at zeroth index: " + str(output))

print("Result: " + str(runProgram(content)))
# print("Result: " + str(runProgram(test)))
# print("Result: " + str(runProgram(test2)))
