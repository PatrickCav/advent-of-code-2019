def getIntArray(input):
    return [int(i) for i in input.split(",")]


infile = open('day2_input.txt', 'r')

content = getIntArray(infile.readline().strip())
# content = [x.strip() for x in content]

print(content)

# test = getIntArray("1,0,0,0,99")
# print(test)

# test2 = getIntArray("1,1,1,4,99,5,6,0,99")

def performStep(startIndex, input):
    value = input[startIndex]
    if value == 1:
        firstIndex = input[startIndex + 1]
        secondIndex = input[startIndex + 2]
        thirdIndex = input[startIndex + 3]
        input[thirdIndex] = input[firstIndex] + input[secondIndex]
        return performStep(startIndex + 4, input)
    elif value == 2:
        firstIndex = input[startIndex + 1]
        secondIndex = input[startIndex + 2]
        thirdIndex = input[startIndex + 3]
        input[thirdIndex] = input[firstIndex] * input[secondIndex]
        return performStep(startIndex + 4, input)
    elif value == 99:
        return input[0]
    else:
        print("Unknown optcode: " + str(value))
        return -1

def runProgram(input, noun, verb):
    input[1] = noun
    input[2] = verb
    output = performStep(0, input)
    # print("Value at zeroth index: " + str(output))
    return output

def runUpToMax(maxIndex):
    for i in range(0, maxIndex):
        for j in range(0, maxIndex):
            testInput = list(content)
            if runProgram(testInput, i, j) == 19690720:
                result = ((100 * i) + j)
                return result

# print("Test: " + str(runProgram(content, 12, 2)))
print("Result: " + str(runUpToMax(99)))
            

