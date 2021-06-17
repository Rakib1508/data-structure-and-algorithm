def bfs(data, start, end, visited=[]):
    queue = [start]
    while queue:
        current = queue.pop(0)
        if current == end:
            print('Path: ' + '-->'.join(visited) + '-->' + end)
            return
        visited.append(current)

        for node in data[current] - set(visited):
            queue.append(node)
    print('Path does not exist')
    return


if __name__ == '__main__':
    data = {
        'A': {'B'},
        'B': {'C', 'D'},
        'C': {'E'},
        'D': {'E'},
        'E': {'F'},
        'F': set()
    }
    bfs(data, 'A', 'D')
