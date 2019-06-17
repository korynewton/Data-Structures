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
        if len(self.storage) > 1:
            # store item to be deleted
            delete = self.get_max()

            # swap top and bottom
            self.storage[0] = self.storage[-1]

            # delete bottom
            del self.storage[-1]

            # sift down new top item
            self._sift_down(0)

        elif len(self.storage) <= 1:
            delete = self.storage[0]
            del self.storage[0]

        # else:
        #     return False

        return delete

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):

        while index > 0:
            # keep bubbling up until we've either reached the top of the heap or a parent that is grater than node
            parent = (index - 1)//2
            if self.storage[index] > self.storage[parent]:
                # swap em
                self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]

                # update index for next loop, node we are bubbling is now at index where parent was
                index = parent
            else:
                    # break out of while loop because it is in correct spot
                break

    def _sift_down(self, index):
        left_child = index * 2 + 1
        right_child = index * 2 + 2

        maximum = index

        if len(self.storage) > left_child and self.storage[maximum] < self.storage[left_child]:
            maximum = left_child
        if len(self.storage) > right_child and self.storage[maximum] < self.storage[right_child]:
            maximum = right_child

        if maximum != index:
            self.storage[index], self.storage[maximum] = self.storage[maximum], self.storage[index]
            self._sift_down(maximum)


# test = Heap()
# print(len(test.storage))
# test.insert(5)
# print(len(test.storage))
