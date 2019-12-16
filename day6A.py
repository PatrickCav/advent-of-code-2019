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
    # childNode.parents = parentNode.parents + 1
    # parentNode.children = parentNode.children + 1

print("{0} total nodes".format(len(nodeMap.values())))

def orbitCount(node):
    if node.parent is None:
        print("Node {0} has no parent".format(node.name))
        return 0
    else:
        return 1 + orbitCount(node.parent)

orbits = 0

for node in nodeMap.values():
    orbits += orbitCount(node)

print("{0} total orbits".format(orbits))