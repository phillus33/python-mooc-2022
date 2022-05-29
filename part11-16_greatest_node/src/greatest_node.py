# WRITE YOUR SOLUTION HERE:
from turtle import left


class Node:
    """ Class is modeling single node in binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

def greatest_node(root: Node):
    curr_val = root.value

    if root.left_child:
        left_val = greatest_node(root.left_child)
    else:
        left_val = curr_val
    
    if root.right_child:
        right_val = greatest_node(root.right_child)
    else:
        right_val = curr_val

    return max(curr_val, left_val, right_val)

    
    
    # not so recursive solution
    # max_node = root.value

    # if root.left_child is not None:
    #     if greatest_node(root.left_child) > max_node:
    #         max_node = greatest_node(root.left_child)
    #     greatest_node(root.left_child)

    # if root.right_child is not None:
    #     if greatest_node(root.right_child) > max_node:
    #         max_node = greatest_node(root.right_child)
    #     greatest_node(root.right_child)

    # return max_node