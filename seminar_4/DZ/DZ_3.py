class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.color = "red"

class RedBlackTree:

    RED = "red"
    BLACK = "black"

    def __init__(self):
        self.root = None

    def left_rotate(self, my_node):
        child = my_node.right
        child_left = child.left
        child.left = my_node
        my_node.right = child_left
        return child

    def right_rotate(self, my_node):
        child = my_node.left
        child_right = child.right
        child.right = my_node
        my_node.left = child_right
        return child

    def red(self, my_node):
        return my_node != None and my_node.color == RedBlackTree.RED

    def color_swap(self, node1, node2):
        temp = node1.color
        node1.color = node2.color
        node2.color = temp

    def insert(self, data):
        if self.root:
            node = self.insert_balance(self.root, data)
            if not node:
                return False
        else:
            node = Node(data)
        self.root = node
        self.root.color = RedBlackTree.BLACK
        return True

    def insert_balance(self, my_node, data):
        if my_node == None:
            return Node(data)
        if my_node.data > data:
            my_node.left = self.insert_balance(my_node.left, data)
        elif my_node.data < data:
            my_node.right = self.insert_balance(my_node.right, data)
        else:
            return None
        return self.balanced(my_node)

    def balanced(self, my_node):
        if self.red(my_node.right) and not self.red(my_node.left):
            my_node = self.left_rotate(my_node)
            self.color_swap(my_node, my_node.left)
        if self.red(my_node.left) and self.red(my_node.left.left):
            my_node = self.right_rotate(my_node)
            self.color_swap(my_node, my_node.right)
        if self.red(my_node.left) and self.red(my_node.right):
            my_node.color = RedBlackTree.RED
            my_node.left.color = RedBlackTree.BLACK
            my_node.right.color = RedBlackTree.BLACK
        return my_node

    def print_tree(self,node):
        if node is not None:
            self.print_tree(node.right)
            print(str(node.data) + ' -> ' + node.color)
            self.print_tree(node.left)

if __name__ == "__main__":
     node = RedBlackTree()
     node.insert(10)
     node.print_tree(node.root)
     node.insert(30)
     node.print_tree(node.root)
     node.insert(20)
     node.print_tree(node.root)
     node.insert(60)
     node.print_tree(node.root)
     node.insert(40)
     node.print_tree(node.root)