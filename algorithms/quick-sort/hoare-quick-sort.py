def swap(i, j, array):
    if i != j:
        temp = array[i]
        array[i] = array[j]
        array[j] = temp


def partition(elements, start, end):
    index = start
    pivot = elements[index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1
        while elements[end] > pivot:
            end -= 1
        if start < end:
            swap(start, end, elements)

    swap(index, end, elements)
    return end


def quick_sort(items, start, end):
    if start < end:
        index = partition(items, start, end)
        quick_sort(elements, start, index-1)
        quick_sort(elements, index+1, end)


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
