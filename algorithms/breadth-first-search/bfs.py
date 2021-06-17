def bfs(data, start, visited=set()):
    queue = [start]
    while queue:
        current = queue.pop(0)
        if current not in visited:
            print(current, end=' ')
        visited.add(current)

        for node in data[current] - visited:
            queue.append(node)
    return


if __name__ == '__main__':
    data = {
        'A': {'B'}, 'B': {'A', 'C', 'D'},
        'C': {'B', 'E'}, 'D': {'B', 'E'},
        'E': {'C', 'D', 'F'}, 'F': {'E'}
    }

    bfs(data, 'A')
