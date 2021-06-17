# Merge Sort

Modify [merge_sort function](https://github.com/Rakib1508/data-structure-and-algorithm/blob/master/algorithms/merge-sort/merge-sort.py) such that it can sort following list of athletes as per the time taken by them in the marathon,

```
elements = [
        { 'name': 'emon',   'age': 17, 'time_hours': 1},
        { 'name': 'zaman', 'age': 12,  'time_hours': 3},
        { 'name': 'saif',  'age': 21,  'time_hours': 2.5},
        { 'name': 'raju',  'age': 24,  'time_hours': 1.5},
    ]
```

merge_sort function should take key from an athlete's marathon log and sort the list as per that key. For example,

```
merge_sort(elements, key='time_hours', descending=True)
```

This will sort elements by time_hours and your sorted list will look like,

```
elements = [
        {'name': 'zaman', 'age': 12, 'time_hours': 3},
        {'name': 'saif', 'age': 21, 'time_hours': 2.5},
        {'name': 'raju', 'age': 24, 'time_hours': 1.5},
        {'name': 'emon', 'age': 17, 'time_hours': 1},
    ]
```

But if you call it like this,

```
merge_sort(elements, key='name')
```

output will be,

```
elements = [
        { 'name': 'raju',   'age': 24, 'time_hours': 1.5},
        { 'name': 'zaman', 'age': 12,  'time_hours': 3},
        { 'name': 'emon',  'age': 17,  'time_hours': 1},
        { 'name': 'saif',  'age': 21,  'time_hours': 2.5},
    ]
```
