def swap(i, j, array):
    if i != j:
        array[i], array[j] = array[j], array[i]


def partition(items, start, end):
    pivot = items[end]
    p_index = start
    for i in range(start, end):
        if items[i] <= pivot:
            print('Before:', items)
            swap(i, p_index, items)
            p_index += 1
            print('After:', items)
    swap(p_index, end, items)
    return p_index


def quick_sort(items, start, end):
    if len(items) == 1:
        return
    if start < end:
        index = partition(items, start, end)
        quick_sort(items, start, index-1)
        quick_sort(items, index+1, end)


if __name__ == '__main__':
    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        quick_sort(elements, 0, len(elements)-1)
        print(f'sorted array: {elements}')
