with open('day1_input.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]

previousChar = ""

def getFuel(input):
    required = (input / 3) - 2
    # print(required)
    if required >= 2:
        return required + getFuel(required)
    else:
        return max(0, required)

print(getFuel(1969))

count = 0

for entry in content:
    count += getFuel(int(entry))

print(count)
