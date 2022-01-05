# Stack simply works in a last in first out (LIFO) fashion.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        if not self.items:      # check if items == []
            return True
        return False


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    while not s.is_empty():
        item = s.pop()
        print(item)


""" Complexity

** push & pop both method time complexity complexity ---> O(1)
** Stack data structure space complexity ---> O(n)

"""