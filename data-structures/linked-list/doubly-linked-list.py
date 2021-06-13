class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    number_of_nodes = 0

    def __init__(self):
        self.head = None

    def print_forward(self):
        if self.head is None:
            print('Linked List is empty')
            return

        iter = self.head
        result = ''
        while iter:
            result += str(iter.data) + '-->'
            iter = iter.next
        print(result)

    def print_backward(self):
        if self.head is None:
            print('Linked List is empty')
            return

        iter = self.get_last_node()
        result = ''
        while iter:
            result += str(iter.data) + '-->'
            iter = iter.prev
        print('Linked List in reverse:', result)

    def get_last_node(self):
        iter = self.head
        while iter.next:
            iter = iter.next
        return iter

    def insert_head(self, data):
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
            self.number_of_nodes += 1
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node
            self.number_of_nodes += 1

    def insert_tail(self, data):
        if self.head is None:
            self.head = Node(data, self.head, None)
            self.number_of_nodes += 1
            return

        iter = self.head
        while iter.next:
            iter = iter.next
        iter.next = Node(data, None, iter)
        self.number_of_nodes += 1

    def insert(self, index, data):
        if index < 0 or index > self.number_of_nodes:
            raise Exception('Invalid index')
        if index == 0:
            self.insert_head(data)
            return

        count = 0
        iter = self.head
        while iter:
            if count == index-1:
                node = Node(data, iter.next, iter)
                if node.next:
                    node.next.prev = node
                iter.next = node
                self.number_of_nodes += 1
                break
            iter = iter.next
            count += 1

    def remove(self, index):
        if index < 0 or index >= self.number_of_nodes:
            raise Exception('Invalid index')
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            self.number_of_nodes -= 1
            return

        count = 0
        iter = self.head
        while iter:
            if count == 0:
                iter.prev.next = iter.next
                if iter.next:
                    iter.next.prev = iter.prev
                self.number_of_nodes -= 1
                break
            iter = iter.next
            count += 1

    def insert_values(self, dataset):
        self.head = None
        for data in dataset:
            self.insert_tail(data)


if __name__ == '__main__':
    items = DoublyLinkedList()
    items.insert_values(['banana', 'mango', 'grapes', 'orange'])
    items.print_forward()
    items.print_backward()
    items.insert_tail('figs')
    items.print_forward()
    items.insert(0, 'jackfruits')
    items.print_forward()
    items.print_backward()
    items.insert(6, 'dates')
    items.print_forward()
    items.print_backward()
    items.insert(2, 'kiwi')
    items.print_forward()
    items.print_backward()
