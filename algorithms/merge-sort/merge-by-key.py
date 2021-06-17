def merge_sort(items, key, asc=True):
    size = len(items)
    if size == 1:
        return items
    splitter = len(items) // 2
    left = merge_sort(items[:splitter], key, asc)
    right = merge_sort(items[splitter:], key, asc)
    return merger(left, right, key, asc)


def merger(left_list, right_list, key, asc=True):
    merged_list = []
    if asc:
        while len(left_list) > 0 and len(right_list) > 0:
            if left_list[0][key] <= right_list[0][key]:
                merged_list.append(left_list.pop(0))
            else:
                merged_list.append(right_list.pop(0))
    else:
        while len(left_list) > 0 and len(right_list) > 0:
            if left_list[0][key] >= right_list[0][key]:
                merged_list.append(left_list.pop(0))
            else:
                merged_list.append(right_list.pop(0))

    merged_list.extend(left_list)
    merged_list.extend(right_list)
    return merged_list


if __name__ == '__main__':
    elements = [
        {'name': 'emon',   'age': 17, 'time_hours': 1},
        {'name': 'zaman', 'age': 12,  'time_hours': 3},
        {'name': 'saif',  'age': 21,  'time_hours': 2.5},
        {'name': 'raju',  'age': 24,  'time_hours': 1.5},
    ]

    sorted_list = merge_sort(elements, key='time_hours', asc=False)
    print(sorted_list)
