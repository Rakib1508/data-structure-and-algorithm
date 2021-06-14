class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        hash_value = 0
        for ch in key:
            hash_value += ord(ch)
        return hash_value % self.MAX

    def get_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0, index)]

    def find_slot(self, key, index):
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return prob_index
            if self.arr[prob_index][0] == key:
                return prob_index
        raise Exception('HashTable full')

    def __getitem__(self, key):
        hash = self.get_hash(key)
        if self.arr[hash] in None:
            return
        prob_range = self.get_prob_range(hash)
        for prob_index in prob_range:
            element = self.arr[prob_index]
            if element is None:
                return
            if element[0] == key:
                return element[1]

    def __setitem__(self, key, value):
        hash = self.get_hash(key)
        if self.arr[hash] is None:
            self.arr[hash] = (key, value)
        else:
            new_hash = self.find_slot(key, hash)
            self.arr[new_hash] = (key, value)

    def __delitem__(self, key):
        hash = self.get_hash(key)
        prob_range = self.get_prob_range(hash)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return
            if self.arr[prob_index][0] == key:
                self.arr[prob_index] = None
        print(self.arr)


if __name__ == '__main__':
    print([*range(5, 8)] + [*range(0, 4)])
    t = HashTable()
    print(t.arr)
    t['march 6'] = 20
    print(t.arr)
    t['march 17'] = 88
    print(t.arr)
    t['march 17'] = 29
    print(t.arr)
    t['nov 1'] = 1
    print(t.arr)
    t['march 33'] = 234
    print(t.arr)
    t['march 33'] = 999
    print(t.arr)
    t['april 1'] = 87
    print(t.arr)
    t['april 2'] = 123
    print(t.arr)
    t['april 3'] = 234234
    print(t.arr)
    del t['april 2']
    print(t.arr)
