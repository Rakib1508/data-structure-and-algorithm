from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


def reverse_string(string):
    stack = Stack()
    for ch in string:
        stack.push(ch)
    reverse = ''
    while True:
        reverse += stack.pop()
        if stack.is_empty():
            break
    return reverse


if __name__ == '__main__':
    print(reverse_string('We should be humble'))
    print(reverse_string('I am a believer'))
