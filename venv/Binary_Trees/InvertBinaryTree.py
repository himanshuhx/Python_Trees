#Recursive Approach
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        root.left,root.right=self.invertTree(root.right),self.invertTree(root.left)
        return root

# DFS Approach
#swapping the nodes before adding them to stack
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        stack=[]
        stack.append(root)
        while stack:
            node=stack.pop()
            temp=node.right
            node.right=node.left
            node.left=temp
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root

# BFS Approach
from collections import deque
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        queue=deque()
        queue.append(root)
        while queue:
            node=queue.popleft()
            temp=node.left
            node.left=node.right
            node.right=temp
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root