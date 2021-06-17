def merger(a, b):
    sorted_list = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1

    while i < len(a):
        sorted_list.append(a[i])
        i += 1
    while j < len(b):
        sorted_list.append(b[j])
        j += 1

    return sorted_list


def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merger(left, right)


if __name__ == '__main__':
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9, 8, 7, 2],
        [1, 2, 3, 4, 5]
    ]

    for test in test_cases:
        print(merge_sort(test))
