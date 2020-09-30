#Doing an Inoder traversal Level oder will not work in some cases.
#Appending the curr node to leaf_list whenever we hit left and right as NONE.
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def helper(root,leaf_list):
            stack,curr=[],root
            while curr or stack:
                while curr:
                    stack.append(curr)
                    curr=curr.left
                curr=stack.pop()
                if not curr.left and not curr.right:
                    leaf_list.append(curr.val)
                if curr:
                    curr=curr.right
            return leaf_list
        #print(helper(root1,[]))
        #print(helper(root2,[]))
        return helper(root1,[])==helper(root2,[])