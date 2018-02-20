# queuey.py

from collections import deque

class Queuey:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.items = deque()

    def get(self):
        return self.items.popleft()

    def put(self, item):
        if len(self.items) < self.maxsize:
            self.items.append(item)
        else:
            print('No')


if __name__ == '__main__':
    q = Queuey(2)
    q.put(1)
    q.put(2)
    print(q.get())