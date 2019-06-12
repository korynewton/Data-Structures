class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Compare the element against the current nodes value
        # based on the result of the comparison, go left or right
        if value < self.value:
            if not self.left:
                #  base case: once reaches end, start new branch
                self.left = BinarySearchTree(value)
            else:
              # recursive case: run insert method again from self.left object, do this recursively until it finds a space
                self.left.insert(value)
        if value > self.value:
            if not self.right:
                # base case: park node here
                self.right = BinarySearchTree(value)
            else:
              # recursive case
                self.right.insert(value)

    def contains(self, target):
        pass

    def get_max(self):
        pass

    def for_each(self, cb):
        pass


test = BinarySearchTree(5)
print(test.value)  # 5
print(test.left)  # None
print(test.right)  # None
