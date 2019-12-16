inputFile = 'day6_input.txt'
# inputFile = 'day6_test_input.txt'

with open(inputFile) as f:
    content = f.readlines()

content = [x.strip() for x in content]

# print(content)

class Node:
    name = ""
    parent = None
    # children = 0
    # parents = 0

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent

    # def __repr__(self):
    #     return "{0} has {1} child, {2} parents.".format(self.name, self.children, self.parents)

    # def __str__(self):
    #     return "{0} has {1} child, {2} parents.".format(self.name, self.children, self.parents)


nodeMap = {}

for entry in content:
    temp = entry.split(")")
    parent = temp[0]
    child = temp[1]
    # print(child + " is in orbit around: " + parent)
    if parent in nodeMap:
        parentNode = nodeMap[parent]
    else:
        parentNode = Node(parent, None)
        nodeMap[parent] = parentNode

    if child in nodeMap:
        childNode = nodeMap[child]
        childNode.parent = parentNode
    else:
        childNode = Node(child, parentNode)
        nodeMap[child] = childNode

print("{0} total nodes".format(len(nodeMap.values())))

def orbitCount(node):
    if node.parent is None:
        return 0
    else:
        return 1 + orbitCount(node.parent)

san = nodeMap["SAN"]
you = nodeMap["YOU"]
sanOrbits = orbitCount(san)
youOrbits = orbitCount(you)

print("SAN total orbits: {0}. YOU total orbits: {1}".format(sanOrbits, youOrbits))

def getOrbitPath(node):
    path = []
    current = node
    while current is not None:
        path.append(current.name)
        current = current.parent
    return path


sanPath = getOrbitPath(san)
youPath = getOrbitPath(you)
sanPath.reverse()
youPath.reverse()

count = 0

sanNode = sanPath[count]
youNode = youPath[count]

while sanNode == youNode:
    count += 1
    sanNode = sanPath[count]
    youNode = youPath[count]

total = sanOrbits + youOrbits - (2 * count)

print(str(total))