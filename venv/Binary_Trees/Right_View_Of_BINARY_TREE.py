# A level order Traversal with appending NONE at end of each level
# all we want is the node just before NONE as it will give the right view
# also we are maintaining a prev node reference which keeps tract of the
# prev node, we append it to our ans List as soon we hit NONE this depicts
# the end of current level and tells that next level children are already in queue.

from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return
        queue, ans, prev = deque(), [], root
        queue.append(root)
        queue.append(None)
        while len(queue) > 1:
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    prev = node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                else:
                    queue.append(None)
                    ans.append(prev)
        return ans

#DFS approach
#          1
#       /     \
#      4       5
#       \     /  \
#        8   9   10
# for a tree like this we will have our res list be like [[1],[5,4],[10,9,8]]
# so for every res[i][0] we can get the right most node as 1  5 10

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        self.dfs(root, 0, res)
        print(res)
        return [x[0] for x in res]

    def dfs(self, root, level, res):
        if root:
            if len(res) < level + 1:
                res.append([])
            res[level].append(root.val)
            self.dfs(root.right, level + 1, res)
            self.dfs(root.left, level + 1, res)



