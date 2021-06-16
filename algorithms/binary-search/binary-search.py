from util import stopwatch


@stopwatch
def linear_search(numbers, target):
    for index, number in enumerate(numbers):
        if number == target:
            return index
    return -1


@stopwatch
def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1
    mid = 0

    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


@stopwatch
def binary_search_recursive(numbers, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2
    if mid >= len(numbers) or mid < 0:
        return -1

    if numbers[mid] == target:
        return mid
    elif numbers[mid] < target:
        return binary_search_recursive(numbers, target, mid+1, right)
    else:
        return binary_search_recursive(numbers, target, left, mid-1)


def find_all(numbers, target):
    index = binary_search(numbers, target)
    positions = [index]

    i = index - 1
    while i >= 0:
        if numbers[i] == target:
            positions.append(i)
        break

    i = index + 1
    while i < len(numbers):
        if numbers[i] == target:
            positions.append(i)
        break
    return sorted(positions)


if __name__ == '__main__':
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 21

    index = linear_search(numbers_list, number_to_find)
    print(f"Number found at index {index} using linear search")

    index = binary_search(numbers_list, number_to_find)
    print(f"Number found at index {index} using binary search")

    index = binary_search_recursive(
        numbers_list, number_to_find, 0, len(numbers_list)-1)
    print(f"Number found at index {index} using binary search")

    numbers = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    target = 15
    print('Occurances at:', find_all(numbers, target))
