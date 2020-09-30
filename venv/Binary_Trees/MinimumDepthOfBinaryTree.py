#Level Order Traversal
#keeping track of current level and if we hit a leaf node update min_depth and break
from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue=deque()
        level,min_depth=0,0
        queue.append(root)
        queue.append(None)
        while queue:
            curr=queue.popleft()
            if not curr:
                level+=1
                if queue:
                    queue.append(None)
                else:
                    break
            else:
                if not curr.left and not curr.right:
                    min_depth=level
                    break
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return min_depth+1

#Recursive Approach
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        #base case
        if not root:
            return 0
        #if only right child present get depth of it by dfs
        if not root.left:
            return self.minDepth(root.right)+1
        #if only left child present get depth of it by dfs
        elif not root.right:
            return self.minDepth(root.left)+1
        #if both are present get min from two
        else:
            return min(self.minDepth(root.right),self.minDepth(root.left))+1