# Queue simply works in FIFO
class Queue:
    def __init__(self, size):
        self.items = [0] * size
        self.max_size = size
        self.head, self.tail, self.size = 0, 0, 0

    def enqueue(self, item):
        if self.is_list_full():
            print(f'Queue is full')
            return

        print(f'Inserting {item}')
        self.items[self.tail] = item
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1

    def dequeue(self):
        item = self.items[self.head]
        self.head = (self.head + 1) % self.max_size
        self.size -= 1

        return item

    def is_list_full(self):
        if self.size == self.max_size:
            return True
        return False

    def is_empty(self):
        if self.size == 0:
            return True
        return False


if __name__ == '__main__':
    queue = Queue(4)

    queue.enqueue('Muhammad')
    queue.enqueue('Ahamaad')
    queue.enqueue('Al-amin')

    while not queue.is_empty():
        person = queue.dequeue()
        # print(person)
    print(queue.items)
    # print(queue.head)
    # print(queue.tail)


""" Complexity

Circular queue & dequeue both method complexity ---> O(1)
Space complexity ---> O(n)

"""
