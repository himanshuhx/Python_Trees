#Recursive approach
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.ans=[]
        def helper(root):
            if not root:
                return
            helper(root.left)
            self.ans.append(root.val)
            helper(root.right)
        helper(root)
        return self.ans
#Time Complexity - O(n) Iterating each node exactly once
#Auxilary Space - O(h) In worst case all the left most nodes are in Recursion Stack
#Iterative approach
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans,ino=[],[]
        curr=root
        while curr or ans:
            while curr:
                ans.append(curr)
                curr=curr.left
            curr=ans.pop()
            ino.append(curr.val)
            curr=curr.right
        return ino
