# Depth First Search (DFS)

Given a graph containing managers and their employees as a dictionary of sets, print all employees reporting to a given manager.

```
data = {
        "Habib": {"Ashik","Nayeem"},
        "Ashik": {"Ahsan", "Topu"},
        "Topu": {"Nayeem"},
        "Atik": {"Tahmid"},
        "Ahsan" : set(),
        "Nayeem" : set()
}


```

Example: Ashik and Nayeem are reporting to Habib. Ahsan and Topu are reporting to Ashik.

```
Q. Find all employees who are reporting to Habib.
```

**Explanation:**

-So here, we want to find all the children nodes of Habib.

-We will perform DFS starting on Habib and then traverse all the children of Habib which are unvisited.

**Output:**

Habib : Nayeem Ashik Ahsan Topu
