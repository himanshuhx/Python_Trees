#Recursive aprroach
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.ans=[]
        def helper(root):
            if not root:
                return
            self.ans.append(root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        return self.ans
#Iterative Approach
#curr.left until we hit null also keep appending the root values
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        pre,stack=[],[]
        curr=root
        while curr or stack:
            while curr:
                pre.append(curr.val)
                stack.append(curr)
                curr=curr.left
            curr=stack.pop()
            curr=curr.right
        return pre