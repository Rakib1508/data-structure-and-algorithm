class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    number_of_nodes = 0

    def __init__(self):
        self.head = None

    def print_nodes(self):
        if self.head is None:
            print('Linked List is empty')
            return
        iter = self.head
        result = ''
        while iter:
            result += str(iter.data) + '-->'
            iter = iter.next
        print(result)

    def insert_head(self, data):
        node = Node(data, self.head)
        self.head = node
        self.number_of_nodes += 1

    def insert_tail(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.number_of_nodes += 1
            return

        iter = self.head
        while iter.next:
            iter = iter.next
        iter.next = Node(data, None)
        self.number_of_nodes += 1

    def insert(self, index, data):
        if index < 0 or index > self.number_of_nodes:
            raise Exception('Invalid Index')

        if index == 0:
            self.insert_head(data)
            return

        count = 0
        iter = self.head
        while iter:
            if count == index-1:
                node = Node(data, iter.next)
                iter.next = node
                self.number_of_nodes += 1
                break
            iter = iter.next
            count += 1

    def remove_head(self):
        self.head = self.head.next
        self.number_of_nodes -= 1

    def remove_tail(self):
        if self.head is None:
            raise Exception('No item found')

        count = 0
        iter = self.head
        while iter:
            if count < self.number_of_nodes-1:
                iter = iter.next
            else:
                iter.next = None
                self.number_of_nodes -= 1
                break

    def remove(self, index):
        if index < 0 or index >= self.number_of_nodes:
            raise Exception('Invalid Index')
        if index == 0:
            self.head = self.head.next
            # self.remove_head()
            self.number_of_nodes -= 1
            return

        count = 0
        iter = self.head
        while iter:
            if count == index-1:
                iter.next = iter.next.next
                self.number_of_nodes -= 1
                break
            iter = iter.next
            count += 1

    def insert_values(self, dataset):
        self.head = None
        for data in dataset:
            self.insert_tail(data)

    def insert_after_value(self, data_after, insert_data):
        if self.head is None:
            return
        if self.head.data == data_after:
            self.head.next = Node(insert_data, self.head.next)
            self.number_of_nodes += 1
            return

        iter = self.head
        while iter:
            if iter.data == data_after:
                iter.next = Node(insert_data, iter.next)
                self.number_of_nodes += 1
                break
            iter = iter.next

    def remove_by_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            self.number_of_nodes -= 1
            return

        iter = self.head
        while iter.next:
            if iter.next.data == data:
                iter.next = iter.next.next
                self.number_of_nodes -= 1
                break
            iter = iter.next


if __name__ == '__main__':
    items = LinkedList()
    items.insert_values(['banana', 'mango', 'grapes', 'orange'])
    items.print_nodes()
    items.insert_after_value("mango", "apple")
    items.print_nodes()
    items.remove_by_value("orange")
    items.print_nodes()
    items.remove_by_value("figs")
    items.print_nodes()
    items.remove_by_value("banana")
    items.print_nodes()
    items.remove_by_value("mango")
    items.print_nodes()
    items.remove_by_value("apple")
    items.print_nodes()
    items.remove_by_value("grapes")
    items.print_nodes()
