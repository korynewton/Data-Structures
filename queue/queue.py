class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_next(self):
        return self.next_node

    def get_value(self):
        return self.value

    def set_next(self, node):
        self.next_node = node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Will be used to enque new nodes to back of linked list
    def add_to_tail(self, value):
        new_node = Node(value)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    # Will be used to deque head node of linked list
    def remove_head(self):
        if not self.head and not self.tail:
            return None
        if self.head is self.tail:
            prev_head = self.head
            self.head = None
            self.tail = None
            return prev_head.get_value()
        else:
            new_head = self.head.get_next()
            old_head = self.head
            self.head = new_head
            return old_head.get_value()


class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = LinkedList()

    def enqueue(self, item):
        self.size += 1
        # self.storage.append(item)
        self.storage.add_to_tail(item)

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            # return self.storage.pop(0)
            return self.storage.remove_head()
        else:
            return None

    def len(self):
        return self.size


q = Queue()
print(q.size)
q.enqueue(100)
q.enqueue(101)
q.enqueue(105)
print(q.size)
print(q.dequeue())
print(q.size)
print(q.dequeue())
