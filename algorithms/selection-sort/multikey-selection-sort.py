def multikey_selection_sort(items, keys):
    for key in keys[-1::-1]:
        for x in range(len(items)):
            min_index = x
            for y in range(x, len(items)):
                if items[y][key] < items[min_index][key]:
                    min_index = y
            if x != min_index:
                items[x], items[min_index] = items[min_index], items[x]


if __name__ == '__main__':
    elements = [
        {'First Name': 'Adnan', 'Last Name': 'Ahmed'},
        {'First Name': 'Amin', 'Last Name': 'Mahmud'},
        {'First Name': 'Emon', 'Last Name': 'Khan'},
        {'First Name': 'Jahid', 'Last Name': 'Bhuiyan'},
        {'First Name': 'Jahid', 'Last Name': 'Hassan'},
        {'First Name': 'Labib', 'Last Name': 'Abdullah'},
        {'First Name': 'Mustafa', 'Last Name': 'Chowdhury'},
        {'First Name': 'Rafi', 'Last Name': 'Majumdar'},
        {'First Name': 'Rafi', 'Last Name': 'Talukdar'},
        {'First Name': 'Rafiq', 'Last Name': 'Hossain'},
        {'First Name': 'Saif', 'Last Name': 'Ahmed'},
        {'First Name': 'Saif', 'Last Name': 'Nayeem'},
        {'First Name': 'Sayeed', 'Last Name': 'Ahmed'},
        {'First Name': 'Shobuj', 'Last Name': 'Hasan'},
    ]

    print(f'Given unsorted array:', *elements, sep='\n')
    multikey_selection_sort(
        elements, ['First Name', 'Last Name'])
    print(f'Array after Multi-key Sorting:', *elements, sep='\n')
