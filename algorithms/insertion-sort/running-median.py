def insert_to(array, key):
    index = 0
    for item in array:
        if item > key:
            break
        index += 1
    return array[:index] + [key] + array[index:]


if __name__ == '__main__':
    array = [2, 1, 5, 7, 2, 0, 5]
    stream = []
    count = 0
    while True:
        i = int(input())
        count += 1
        stream = insert_to(array, i)
        if count % 2 == 1:
            print(f'Median of {stream} : {stream[count//2]}')
        else:
            i1 = count // 2
            i2 = (count//2) - 1
            print(f'Median of {stream} : {(stream[i1] + stream[i2]) / 2}')
