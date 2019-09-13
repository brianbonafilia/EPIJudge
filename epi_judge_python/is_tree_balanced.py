from test_framework import generic_test

balanced = True 

def is_balanced_binary_tree(tree):
    # TODO - you fill in here.
    return balanced_helper(0, tree)[0]

def balanced_helper(height, node):
    if not node:
        return True, height
    left = balanced_helper(height + 1, node.left)
    right = balanced_helper(height + 1, node.right)
    if left[0] and right[0] and abs(left[1] - right[1]) < 2:
        return True, max(left[1], right[1])
    else:
        return False, None
    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
