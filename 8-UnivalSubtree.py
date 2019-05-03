class Node:
    
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

# Boolean function to check whether a node is unival
def is_unival_subtree(node, count):

    if not node:
        return True
    
    left_unival = is_unival_subtree(node.left, count)
    right_unival = is_unival_subtree(node.right, count)

    # Leaf node
    if (not node.left and not node.right):
        count[0] += 1
        return True

    # Left and right are unival subtrees, and value of root is same
    if (left_unival and right_unival and node.key == node.left.key and node.key == node.right.key):
        count[0] += 1
        return True

    # Only right child exists
    if ((not node.left) and right_unival and node.right.key == node.key):
        count[0] += 1
        return True

    # Only left child exists
    if ((not node.right) and left_unival and node.left.key == node.key):
        count[0] += 1
        return True

    return False

# Main recursive function
def count_unival_subtree(root):
    count = [0]
    is_unival_subtree(root, count)
    return count[0]

node = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
assert count_unival_subtree(node) == 5