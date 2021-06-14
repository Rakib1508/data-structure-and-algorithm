import threading
import time
from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, value):
        self.buffer.appendleft(value)

    def dequeue(self):
        if len(self.buffer) == 0:
            print('Queue is empty')
            return
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def front(self):
        return self.buffer[-1]


food_court_queue = Queue()


def place_order(orders):
    for order in orders:
        print('Placing order for:', order)
        food_court_queue.enqueue(order)
        time.sleep(0.5)


def serve_orders():
    time.sleep(1)
    while True:
        order = food_court_queue.dequeue()
        print('Now serving:', order)
        time.sleep(2)


if __name__ == '__main__':
    orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
    thread1 = threading.Thread(target=place_order, args=(orders,))
    thread2 = threading.Thread(target=serve_orders)

    thread1.start()
    thread2.start()
