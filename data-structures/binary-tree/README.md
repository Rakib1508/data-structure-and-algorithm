# Binary Tree

Here are the list of methods implemented in this module for Binary Search Tree or BST

    1. find_min(): finds minimum element in entire binary tree
    2. find_max(): finds maximum element in entire binary tree
    3. calculate_sum(): calcualtes sum of all elements
    4. post_order_traversal(): performs post order traversal of a binary tree
    5. pre_order_traversal(): perofrms pre order traversal of a binary tree

After implementing all these functionality, move on to implement delete functionality to the tree as follows:

```
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

          --->  min_val = self.right.find_min()
          --->  self.data = min_val
          --->  self.right = self.right.delete(min_val)
```
