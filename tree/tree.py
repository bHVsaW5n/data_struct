"""
description: 一棵普通的树, 广度遍历所有的节点，并且打印行号
author: Eileen
data: 2020/9/18
struct of deamon_tree
     10
   /   \
  1    2
 /    / \
3    4   5
    /
   6
"""
from queue import Queue


class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


class Tree:
    def __init__(self):
        self.root = None


tree = Tree()
root = Node(10)
node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_5 = Node(5)
node_6 = Node(6)

node_4.left_child = node_6
node_2.left_child = node_4
node_2.right_child = node_5
node_1.left_child = node_3
root.left_child = node_1
root.right_child = node_2
tree.root=root



q = Queue()

root = tree.root
if root:
    line = 1
    q.put((root, line))
    root, line = q.get()
    print(root.value, line)
    while root:
        if root.left_child:
            q.put((root.left_child, line+1))
        if root.right_child:
            q.put((root.right_child, line+1))
        root, line = q.get()
        print(root.value, line)

else:
    line=0
    print(None, 0)



