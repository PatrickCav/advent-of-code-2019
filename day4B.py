# lower = 248345
lower = 248888
upper = 746315
# upper = 250000

i = lower
matching = 0


def doesntIncrease(input):
    # print("Input: " + str(input))
    previous = input[0]
    i = 1
    count = len(input)
    while i < count:
        current = input[i]
        if current < previous:
            return False
        previous = current
        i += 1
    return True


def validAdjacent(input):
    previous = input[0]
    i = 1
    count = len(input)
    adjacentCount = {}
    while i < count:
        current = input[i]
        if current == previous:
            if current in adjacentCount:
                adjacentCount[current] += 1
            else:
                adjacentCount[current] = 1 
        previous = current
        i += 1
    # print("Input: " + str(input) + ". Adjacent count: " + str(adjacentCount))
    for x in adjacentCount.values():
        if x == 1:
            return True
    return False


print("Lower/Upper: " + str(lower) + "/" + str( upper))

while i < upper:
    # print("Current: " + str(i))
    lst = [int(j) for j in str(i)]
    if validAdjacent(lst) and doesntIncrease(lst):
        # print("Match: " + str(i))
        matching += 1
    i += 1


print("Matching count: " + str(matching))
