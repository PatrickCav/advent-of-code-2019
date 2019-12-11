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


def twoAdjacent(input):
    # print("Input: " + str(input))
    previous = input[0]
    i = 1
    count = len(input)
    while i < count:
        current = input[i]
        if current == previous:
            return True
        previous = current
        i += 1
    return False


print("Lower/Upper: " + str(lower) + "/" + str( upper))

while i < upper:
    # print("Current: " + str(i))
    lst = [int(j) for j in str(i)]
    if twoAdjacent(lst) and doesntIncrease(lst):
        # print("Match: " + str(i))
        matching += 1
    i += 1


print("Matching count: " + str(matching))
