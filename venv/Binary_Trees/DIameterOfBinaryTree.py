class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter=0
        def helper(root):
            if not root:
                return 0
            left=helper(root.left)
            right=helper(root.right)
            self.diameter=max(self.diameter,left+right)
            return 1+max(left,right)
        helper(root)
        return self.diameter