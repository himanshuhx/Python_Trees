#Dfs Approach
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        stack = [(root, root.val)]
        num = 0
        while stack:
            cur, p = stack.pop()

            if not cur.left and not cur.right: num += p

            for child in filter(None, [cur.left, cur.right]):
                stack.append((child, (p << 1) + child.val))

        return num
