def find_employees(data, start, employee, visited=set()):
    if start not in visited:
        print(start, end=' ')
        if start == employee:
            print(':', end=' ')
    visited.add(start)

    for i in data[start] - visited:
        find_employees(data, i, visited)
    return


data = {
    "Habib": {"Ashik", "Nayeem"},
    "Ashik": {"Ahsan", "Topu"},
    "Topu": {"Nayeem"},
    "Atik": {"Tahmid"},
    "Ahsan": set(),
    "Nayeem": set()
}

if __name__ == '__main__':
    find_employees(data, "Habib", "Habib")
