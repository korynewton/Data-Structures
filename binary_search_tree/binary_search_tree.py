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
        # check if self.value is target
        if self.value == target:
            return True
        while self.left and self.right:
            # check if self.value is less than target: go right
            if self.value < target:
                # repeat
                return self.right.contains(target)
            # check if self.value is greater than target: go left
            elif self.value > target:
                # repeat
                return self.left.contains(target)
         # else not in BST return false
        else:
            return False

    def get_max(self):
        pass

    def for_each(self, cb):
        pass


test = BinarySearchTree(5)
print(test.value)  # 5
print(test.left)  # None
print(test.right)  # None
test.insert(3)
test.insert(10)
print(test.left.value)  # 3
print(test.right.value)  # 10
# print(test.contains(3))
# print(test.contains(10))
print(test.contains(5))
print(test.contains(3294))
