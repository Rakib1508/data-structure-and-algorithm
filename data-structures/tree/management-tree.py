class Node:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, property_name=''):
        if property_name == 'both':
            value = self.name + ' (' + self.rank + ')'
        elif property_name == 'name':
            value = self.name
        else:
            value = self.rank

        prefix = ' ' * self.get_level() * 4 + ('|--' if self.parent else '')
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.print_tree(property_name)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


def build_tree():
    it_manager = Node('Atik', 'IT Manager')
    it_manager.add_child(Node('Shakib', 'Flutter Specialist'))
    it_manager.add_child(Node('Shadman', 'Django Specialist'))

    cfo = Node('Yasin', 'CFO')
    cfo.add_child(it_manager)
    cfo.add_child(Node('Shakil', 'Financial Adviser'))

    hrm = Node('Saad', 'HR Manager')
    hrm.add_child(Node('Abdul Kader', 'Recruiter'))
    hrm.add_child(Node('Muhammad', 'Project Manager'))

    ceo = Node('BossMan', 'CEO')
    ceo.add_child(cfo)
    ceo.add_child(hrm)

    return ceo


if __name__ == '__main__':
    root = build_tree()
    root.print_tree('name')
    root.print_tree('rank')
    root.print_tree('both')
