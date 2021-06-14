class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        prefix = ' ' * self.get_level() * 4 + ('|--' if self.parent else '')
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


def build_tree():
    root = Node('Electronics')

    laptop = Node('Laptop')
    laptop.add_child(Node('MacBook'))
    laptop.add_child(Node('Surface'))
    laptop.add_child(Node('ThinkPad'))

    cellphone = Node('Cell Phone')
    cellphone.add_child(Node('iPhone'))
    cellphone.add_child(Node('Samsung'))
    cellphone.add_child(Node('Google Pixel'))

    tv = Node('TV')
    tv.add_child(Node('LG'))
    tv.add_child(Node('Sony'))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree()


if __name__ == '__main__':
    build_tree()
