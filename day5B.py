def getIntArray(input):
    return [int(i) for i in input.split(",")]


infile = open('day5_input.txt', 'r')

content = getIntArray(infile.readline().strip())
# content = [x.strip() for x in content]

# print(content)

userInput = 5

test = getIntArray("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9")
print(test)
test2 = getIntArray("3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99")
print(test2)

output = []

def performStep(startIndex, input):
    print("Index: " + str(startIndex) + ". Program: " + str(input))
    instruction = str(input[startIndex]).zfill(5)

    mode1 = int(instruction[2])
    mode2 = int(instruction[1])
    mode3 = int(instruction[0]) 

    value = int(instruction[3:])

    if value == 1:
        # Addition
        firstIndex = input[startIndex + 1]
        secondIndex = input[startIndex + 2]
        thirdIndex = input[startIndex + 3]
        firstValue = input[firstIndex] if mode1 == 0 else firstIndex
        secondValue = input[secondIndex] if mode2 == 0 else secondIndex
        # thirdValue = input[thirdIndex] if mode3 == 0 else thirdIndex
        input[thirdIndex] = firstValue + secondValue
        return performStep(startIndex + 4, input)
    elif value == 2:
        # Multiply
        firstIndex = input[startIndex + 1]
        secondIndex = input[startIndex + 2]
        thirdIndex = input[startIndex + 3]
        firstValue = input[firstIndex] if mode1 == 0 else firstIndex
        secondValue = input[secondIndex] if mode2 == 0 else secondIndex
        # thirdValue = input[thirdIndex] if mode3 == 0 else thirdIndex
        input[thirdIndex] = firstValue * secondValue
        print("Value 2. First Value: " + str(firstValue) + " Second Value: " + str(secondValue))
        return performStep(startIndex + 4, input)
    elif value == 3:
        # Input
        firstIndex = input[startIndex + 1]
        # firstValue = input[firstIndex] if mode1 == 0 else firstIndex
        # print("Value 3. First Value: " + str(firstValue))
        input[firstIndex] = userInput
        return performStep(startIndex + 2, input)
    elif value == 4:
        # Output
        firstIndex = input[startIndex + 1]
        firstValue = input[firstIndex] if mode1 == 0 else firstIndex
        output.append(firstValue)
        return performStep(startIndex + 2, input)
    elif value == 5:
        # Jump if true
        firstIndex = input[startIndex + 1]
        firstValue = input[firstIndex] if mode1 == 0 else firstIndex
        if firstValue != 0:
            secondIndex = input[startIndex + 2]
            secondValue = input[secondIndex] if mode2 == 0 else secondIndex
            return performStep(secondValue, input)
        else:
            return performStep(startIndex + 3, input)
    elif value == 6:
        # Jump if true
        firstIndex = input[startIndex + 1]
        firstValue = input[firstIndex] if mode1 == 0 else firstIndex
        if firstValue == 0:
            secondIndex = input[startIndex + 2]
            secondValue = input[secondIndex] if mode2 == 0 else secondIndex
            return performStep(secondValue, input)
        else:
            return performStep(startIndex + 3, input)
    elif value == 7:
        # less than
        firstIndex = input[startIndex + 1]
        secondIndex = input[startIndex + 2]
        thirdIndex = input[startIndex + 3]
        firstValue = input[firstIndex] if mode1 == 0 else firstIndex
        secondValue = input[secondIndex] if mode2 == 0 else secondIndex
        # thirdValue = input[thirdIndex] if mode3 == 0 else thirdIndex
        if firstValue < secondValue:
            input[thirdIndex] = 1
        else:
            input[thirdIndex] = 0
        return performStep(startIndex + 4, input)
    elif value == 8:
        # equals
        firstIndex = input[startIndex + 1]
        secondIndex = input[startIndex + 2]
        thirdIndex = input[startIndex + 3]
        firstValue = input[firstIndex] if mode1 == 0 else firstIndex
        secondValue = input[secondIndex] if mode2 == 0 else secondIndex
        # thirdValue = input[thirdIndex] if mode3 == 0 else thirdIndex
        if firstValue == secondValue:
            input[thirdIndex] = 1
        else:
            input[thirdIndex] = 0
        return performStep(startIndex + 4, input)
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
