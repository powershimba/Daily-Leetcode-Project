# Maximum Depth of Binary Tree
# Easy

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS
class Solution(object):
    def maxDepth(self, root):

        if root is None:
            return 0

        cur_depth = max(self.maxDepth(root.left), self.maxDepth(root.right))
        return cur_depth + 1


# BFS
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Exeption
        if root is None:
            return 0

        # set queue
        queue = collections.deque([root])
        depth = 0

        # BFS: put children of each node in queue & remove current(parent) nodes in queue
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)                
                if node.right:
                    queue.append(node.right)
        return depth
