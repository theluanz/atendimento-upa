class BSTNode:
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
 
    def get(self, key):
        if self.key == key:
            return self
        node = self.left if key < self.key else self.right
        if node is not None:
            return node.get(key)

root = BSTNode(42)
root.left = BSTNode(10)
root.right = BSTNode(90)
root.left.left = BSTNode(2)

found = root.get(2)
print(found)
