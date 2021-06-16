# Bubble Sort

Bubble sort implemented on different data types, simple to complex.

```
transaction_records = [
        {'customer': 'Shakib', 'name': 'iPhone-10', 'amount': 1000},
        {'customer': 'Jubair', 'name': 'google pixel 4a', 'amount': 400},
        {'customer': 'Alif', 'name': 'asus rog 3', 'amount': 750},
        {'customer': 'Emon', 'name': 'iPhone-8', 'amount': 800}
    ]
```

bubble_sort function should take key from a transaction record and sort the list as per that key. For example,

```
bubble_sort(elements, key='amount')
```

This will sort elements by amount and your sorted list will look like,

```
transaction_records = [
        {'customer': 'Shakib', 'name': 'iPhone-10', 'amount': 1000},
        {'customer': 'Jubair', 'name': 'google pixel 4a', 'amount': 400},
        {'customer': 'Alif', 'name': 'asus rog 3', 'amount': 750},
        {'customer': 'Emon', 'name': 'iPhone-8', 'amount': 800}
    ]
```

But if you call it like this,

```
bubble_sort(elements, key='name')
```

output will be,

```
transaction_records = [
        {'customer': 'Alif', 'name': 'asus rog 3', 'amount': 750},
        {'customer': 'Jubair', 'name': 'google pixel 4a', 'amount': 400},
        {'customer': 'Shakib', 'name': 'iPhone-10', 'amount': 1000}
        {'customer': 'Emon', 'name': 'iPhone-8', 'amount': 800},
    ]
```
