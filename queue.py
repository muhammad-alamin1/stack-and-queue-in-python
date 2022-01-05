# Queue simply works in a first in first out (FIFO)
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        if not self.items:  # check if items == []
            return True
        return False


if __name__ == '__main__':
    queue = Queue()

    queue.enqueue('Muhammad')
    queue.enqueue('Ahamaad')
    queue.enqueue('Al-amin')

    while not queue.is_empty():
        person = queue.dequeue()
        print(person)


"""Complexity

** enqueue method complexity ---> O(1)
** dequeue method complexity ---> O(n)
** Queue space complexity    ---> O(n)

"""