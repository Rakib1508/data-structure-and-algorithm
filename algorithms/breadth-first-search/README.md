# BFS Traversal

BFS Traversal of a graph in python using graph given in dictionary

Implement a function to find whether a path exists for a given set of airline routes. The routes are depicted using graphs as a dictionary of sets, where keys represent as source and elements of sets represent destinations. Print the path if it exists.

Example: A, B, C, D, E, F are the nodes of the graph.

For example, if you are given following data:

```
data = {
        'A': {'B'},
        'B': {'A', 'C', 'D'},
        'C': {'B', 'E'},
        'D': {'B', 'E'},
        'E': {'C', 'D', 'F'},
        'F': {'E'}
}
```

The resultant graph will be:

![alt text](https://github.com/Rakib1508/data-structure-and-algorithm/blob/master/algorithms/breadth-first-search/DFS_BFS_Graph.png)

Example: Source is A, Destination is D.

Expected Output:

```
Path : A->B->D
```
