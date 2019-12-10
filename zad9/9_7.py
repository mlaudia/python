#dopisac funkcje znajdujace najwiekszy i najmniejszy element drzewa

class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def insert(self, node):
        if self.data < node.data:      # na prawo
            if self.right:
                self.right.insert(node)
            else:
                self.right = node
        elif self.data > node.data:    # na lewo
            if self.left:
                self.left.insert(node)
            else:
                self.left = node
        else:
            pass    # ignoruję duplikaty

    def count(self):
        counter = 1
        if self.left:
            counter += self.left.count()
        if self.right:
            counter += self.right.count()
        return counter

    def search(self, data):
        if self.data == data:
            return self
        if data < self.data:
            if self.left:
                return self.left.search(data)
        else:
            if self.right:
                return self.right.search(data)
        return None

class BST:

    def __init__(self):
        self.root = None

    def insert(self, node):
        if self.root:
            self.root.insert(node)
        else:
            self.root = node

    def count(self):
        if self.root:
            return self.root.count()
        else:
            return 0

    def search(self, data):   # zwraca node lub None
        if self.root:
            return self.root.search(data)
        else:
            return None


    def max_bst(self, top):
        node = top
        while node.right:
            node = node.right
        return node.data


    def min_bst(self, top):
        node = top
        while node.left:
            node = node.left
        return node.data
