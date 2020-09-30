#Recursive Approach
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.ans=[]
        def helper(root):
            if not root:
                return
            helper(root.left)
            helper(root.right)
            self.ans.append(root.val)
        helper(root)
        return self.ans
#Iterative Approach
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        pos,stack=[],[root]
        curr=root
        while stack:
            if stack:
                curr=stack.pop()
            if curr:
                pos.append(curr.val)
                stack.append(curr.left)
                stack.append(curr.right)
        return pos[::-1]