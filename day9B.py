def getIntArray(input):
    return [int(i) for i in input.split(",")]


infile = open('day9_input.txt', 'r')

content = getIntArray(infile.readline().strip())
# content = [x.strip() for x in content]

# print(content)

userInput = 2

output = []

relativeOffset = 0

extendedMemory = {}

def getValueAtIndex(input, index):
    if index < len(input):
        return input[index]
    else:
        if index in extendedMemory:
            return extendedMemory[index]
        else:
            if index < 0:
                print("Negative index")
                return None
            else:
                return 0


def setValueAtIndex(input, index, value, mode):
    global extendedMemory

    if mode == 2:
        setIndex = index + relativeOffset
    else:
        setIndex = index

    if setIndex < len(input):
        input[setIndex] = value
    else:
        extendedMemory[setIndex] = value


def getValue(mode, input, index):
    if mode == 0:
        return getValueAtIndex(input, index)
    elif mode == 1:
        return index
    else:
        return getValueAtIndex(input, relativeOffset + index)


def performStep(startIndex, input):
    # print("Index: " + str(startIndex) + ". Relative offset: " + str(relativeOffset) + ". Program: " + str(input))
    instruction = str(input[startIndex]).zfill(5)

    # Mode 0, position mode: = value at index
    # Mode 1, immediate mode: = index
    # Mode 2, relative mode: = value at (index + relativeOffset)

    mode1 = int(instruction[2])
    mode2 = int(instruction[1])
    mode3 = int(instruction[0]) 

    value = int(instruction[3:])

    global relativeOffset

    if value == 1:
        # Addition
        firstIndex = getValueAtIndex(input, startIndex + 1)
        secondIndex = getValueAtIndex(input, startIndex + 2)
        thirdIndex = getValueAtIndex(input, startIndex + 3)
        firstValue = getValue(mode1, input, firstIndex)
        secondValue = getValue(mode2, input, secondIndex)
        setValueAtIndex(input, thirdIndex, firstValue + secondValue, mode3)
        return startIndex + 4
    elif value == 2:
        # Multiply
        firstIndex = getValueAtIndex(input, startIndex + 1)
        secondIndex = getValueAtIndex(input, startIndex + 2)
        thirdIndex = getValueAtIndex(input, startIndex + 3)
        firstValue = getValue(mode1, input, firstIndex)
        secondValue = getValue(mode2, input, secondIndex)
        setValueAtIndex(input, thirdIndex, firstValue * secondValue, mode3)
        print("Value 2. First Value: " + str(firstValue) + " Second Value: " + str(secondValue))
        return startIndex + 4
    elif value == 3:
        # Input
        firstIndex = getValueAtIndex(input, startIndex + 1)
        # firstValue = getValue(mode1, input, firstIndex)
        print("Index: " + str(startIndex) + ". Relative offset: " + str(relativeOffset))
        print("Value 3. First Value: " + str(firstIndex))
        setValueAtIndex(input, firstIndex, userInput, mode1)
        return startIndex + 2
    elif value == 4:
        # Output
        firstIndex = getValueAtIndex(input, startIndex + 1)
        firstValue = getValue(mode1, input, firstIndex)
        print("Index: " + str(startIndex) + ". Relative offset: " + str(relativeOffset))
        print("Value 4. First Value: " + str(firstValue))
        output.append(firstValue)
        return startIndex + 2
    elif value == 5:
        # Jump if true
        firstIndex = getValueAtIndex(input, startIndex + 1)
        firstValue = getValue(mode1, input, firstIndex)
        if firstValue != 0:
            secondIndex = getValueAtIndex(input, startIndex + 2)
            secondValue = getValue(mode2, input, secondIndex)
            return secondValue
        else:
            return startIndex + 3
    elif value == 6:
        # Jump if true
        firstIndex = getValueAtIndex(input, startIndex + 1)
        firstValue = getValue(mode1, input, firstIndex)
        if firstValue == 0:
            secondIndex = getValueAtIndex(input, startIndex + 2)
            secondValue = getValue(mode2, input, secondIndex)
            return secondValue
        else:
            return startIndex + 3
    elif value == 7:
        # less than
        firstIndex = getValueAtIndex(input, startIndex + 1)
        secondIndex = getValueAtIndex(input, startIndex + 2)
        thirdIndex = getValueAtIndex(input, startIndex + 3)
        firstValue = getValue(mode1, input, firstIndex)
        secondValue = getValue(mode2, input, secondIndex)
        if firstValue < secondValue:
            setValueAtIndex(input, thirdIndex, 1, mode3)
        else:
            setValueAtIndex(input, thirdIndex, 0, mode3)
        return startIndex + 4
    elif value == 8:
        # equals
        firstIndex = getValueAtIndex(input, startIndex + 1)
        secondIndex = getValueAtIndex(input, startIndex + 2)
        thirdIndex = getValueAtIndex(input, startIndex + 3)
        firstValue = getValue(mode1, input, firstIndex)
        secondValue = getValue(mode2, input, secondIndex)
        if firstValue == secondValue:
            setValueAtIndex(input, thirdIndex, 1, mode3)
        else:
            setValueAtIndex(input, thirdIndex, 0, mode3)
        return startIndex + 4
    elif value == 9:
        firstIndex = getValueAtIndex(input, startIndex + 1)
        firstValue = getValue(mode1, input, firstIndex)
        relativeOffset += firstValue
        return startIndex + 2
    elif value == 99:
        return -1
    else:
        print("Unknown optcode: " + str(value))
        return -2


def runProgram(input):
    result = 0
    while result >= 0:
        result = performStep(result, input)
    # print("Value at zeroth index: " + str(output))

test = getIntArray("109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99")
print(test)
print("Test count: " + str(len(test)))
test2 = getIntArray("1102,34915192,34915192,7,4,7,99,0")
print(test2)
print("Test2 count: " + str(len(test2)))

print("Result: " + str(runProgram(content)))
# print("Result: " + str(runProgram(test)))
# print("Result: " + str(runProgram(test2)))
