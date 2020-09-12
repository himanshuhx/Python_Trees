"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
#DFS Approach
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        depth = 0
        for child in root.children:
            depth = max(depth, self.maxDepth(child))
        return 1 + depth

#BFS Approach
from collections import deque
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        queue=deque()
        depth=1
        queue.append(root)
        while queue:
            node=queue.popleft()
            for child in node:
                queue.append(child)
            depth+=1