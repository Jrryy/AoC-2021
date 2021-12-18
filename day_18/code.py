class Node(object):
    def __init__(depth, pair, parent):
        self.parent = parent
        self.depth = depth
        if not isinstance(pair[0], int):
            self.left = Node(depth + 1, pair[0], self)
        else:
            self.left = pair[0]
        if not isinstance(pair[1], int):
            self.right = Node(depth + 1, pair[1], self)
        else:
            self.right = pair[1]

def explode(node: Node):
    if node.depth >= 4 and isinstance(node.left, int) and isinstance(node.right, int):
        parent = node.parent
        parent.
    else:
        if isinstance(self.left, Node):
            _left, _right = self.left.explode()
                

with open('input.txt', 'r') as f:
    numbers = [eval(line.strip()) for line in f]

from pprint import pprint as pp

total = numbers[0]
for number in numbers[1:]:
    to_simplify = [total, number]
    tree = Node(1, to_simplify, None)

