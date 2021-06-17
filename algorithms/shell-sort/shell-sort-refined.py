def shell_sort(array):
    div = 2
    size = len(array)
    gap = size // div
    while gap > 0:
        to_delete = []
        for i in range(gap, size):
            anchor = array[i]
            j = i
            while j >= gap and array[j-gap] >= anchor:
                if array[j-gap] == anchor:
                    to_delete.append(j)
                array[j] = array[j-gap]
                j -= gap
            array[j] = anchor
        to_delete = sorted(list(set(to_delete)))
        if to_delete:
            for i in to_delete[-1::-1]:
                del array[i]
        div *= 2
        size = len(array)
        gap = size // div


if __name__ == '__main__':
    elements = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]

    print(f'Given unsorted list: {elements}')
    shell_sort(elements)
    print(f'List after Sorting : {elements}')
