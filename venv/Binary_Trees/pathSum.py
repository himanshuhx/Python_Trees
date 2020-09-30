#DFS + stack
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        stack=[(root,sum)]
        while stack:
            node,sum=stack.pop()
            if not node.right and not node.left and sum==node.val:
                return True
            if node.right:
                stack.append((node.right,sum-node.val))
            if node.left:
                stack.append((node.left,sum-node.val))
        return False

#Recursive approach
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        sum -= root.val
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
