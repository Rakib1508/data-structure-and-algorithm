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

    def print_tree(self, level):
        if self.get_level() > level:
            return
        prefix = ' ' * self.get_level() * 4 + ('|--' if self.parent else '')
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


def build_tree():
    root = Node('Global')

    bd = Node('Bangladesh')

    ctg = Node('Chittagong')
    ctg.add_child(Node('Cumilla'))
    ctg.add_child(Node('Rangamati'))
    ctg.add_child(Node("Cox's Bazar"))

    raj = Node('Rajshahi')
    raj.add_child(Node('Rajshahi'))
    raj.add_child(Node('Rangpur'))
    raj.add_child(Node('Natore'))

    bd.add_child(ctg)
    bd.add_child(raj)

    ksa = Node('Saudi Arabia')

    makkah = Node('Makkah')
    makkah.add_child(Node('Al Haram'))
    makkah.add_child(Node('Arafa'))
    makkah.add_child(Node('Jeddah'))

    madinah = Node('Madinah')
    madinah.add_child(Node('Al Madinah'))
    madinah.add_child(Node('Riyadh'))

    ksa.add_child(makkah)
    ksa.add_child(madinah)

    root.add_child(bd)
    root.add_child(ksa)

    return root


if __name__ == '__main__':
    root = build_tree()
    root.print_tree(3)
