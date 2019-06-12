class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        # if len(self.storage) == 0:
        #     self.storage.append(value)
        # else:
        #     pass
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        # if only one item:
        if len(self.storage) == 1:
            return self.storage.pop()

        current_max = self.storage.pop(0)

        # sift down max node
        self._sift_down(0)

        return current_max

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        # keep bubbling up until we've either reached the top of the heap or a parent that is grater than node
        parent = (index - 1)//2

        while index > 0:
            if self.storage[index] > self.storage[parent]:
                # swap em
                self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]

                # update index for next loop, node we are bubbling is now at index where parent was
                index = parent
            else:
                # break out of while loop because it is in correct spot
                break

    def _sift_down(self, index):
        pass


test = Heap()
print(len(test.storage))
test.insert(5)
print(len(test.storage))
