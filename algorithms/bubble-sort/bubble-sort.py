def bubble_sort(items):
    size = len(items)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if items[j] > items[j+1]:
                temp = items[j]
                items[j] = items[j+1]
                items[j+1] = temp
                swapped = True
        if not swapped:
            break


def bubble_sort_with_key(items, key=None):
    size = len(items)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if items[j][key] > items[j+1][key]:
                temp = items[j]
                items[j] = items[j+1]
                items[j+1] = temp
                swapped = True
        if not swapped:
            break


if __name__ == '__main__':
    numbers = [5, 9, 2, 1, 67, 34, 88, 34]
    bubble_sort(numbers)
    print(numbers)

    names = ['pumpkin', 'eggplant', 'milk', 'apples', 'dinner set']
    bubble_sort(names)
    print(names)

    transaction_records = [
        {'customer': 'Shakib', 'name': 'iPhone-10', 'amount': 1000},
        {'customer': 'Jubair', 'name': 'google pixel 4a', 'amount': 400},
        {'customer': 'Alif', 'name': 'asus rog 3', 'amount': 750},
        {'customer': 'Emon', 'name': 'iPhone-8', 'amount': 800}
    ]
    bubble_sort_with_key(transaction_records, key='amount')
    print(transaction_records)
