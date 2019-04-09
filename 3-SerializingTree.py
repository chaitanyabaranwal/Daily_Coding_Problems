class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node):
    if not node:
        return ''
    if not node.val:
        return ''
    return '[{0},{1},{2}]'.format(node.val, serialize(node.left), serialize(node.right))

def deserialize(string):
    if string == '':
        return None

    cur_index = 1

    root = ''
    while (cur_index < len(string)):
        if string[cur_index] == ',':
            break
        root += string[cur_index]
        cur_index += 1

    cur_index += 1
    left_string, cur_index = returnList(string, cur_index)
    left = deserialize(left_string)

    cur_index += 1
    right_string, cur_index = returnList(string, cur_index)
    right = deserialize(right_string)

    return Node(root, left, right)

def returnList(string, cur_index):
    index = 1
    answer = ''
    for x in string[cur_index:]:
        if index == 0:
            break

        elif x == '[':
            index += 1
        elif x == ']':
            index -= 1
        answer += x
        cur_index += 1
    return answer[:len(answer)-1], cur_index


node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
