from stack import Stack
from queue import Queue
from circular_queue import Queue

if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    while not s.is_empty():
        item = s.pop()
        print(item)

