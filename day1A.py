with open('day1_input.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]

def getFuel(input):
    return (input / 3) - 2

count = 0

print(getFuel(100756))

for entry in content:
    count += getFuel(int(entry))

print(count)
