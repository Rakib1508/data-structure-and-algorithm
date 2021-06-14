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


def is_match(ch1, ch2):
    matcher = {
        ')': '(',
        ']': '[',
        '}': '{',
    }
    return matcher[ch1] == ch2


def is_balanced(string):
    stack = Stack()
    for ch in string:
        if ch in ['(', '{', '[']:
            stack.push(ch)
        if ch in [')', '}', ']']:
            if stack.is_empty():
                return False
            if not is_match(ch, stack.pop()):
                return False
    return stack.size() == 0


if __name__ == '__main__':
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
