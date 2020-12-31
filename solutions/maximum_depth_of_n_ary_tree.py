class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: Node, currentDepth=0) -> int:

        if root is None:
            return currentDepth

        max_depth = currentDepth + 1
        if not root.children:
            return max_depth

        for child in root.children:
            max_depth = max(max_depth, self.maxDepth(child, currentDepth + 1))

        return max_depth


# Tests
a = Node(1)
b = Node(3)
c = Node(2)
d = Node(4)
a.children = [b, c, d]
e = Node(5)
f = Node(6)
b.children = [e, f]

s = Solution()
assert s.maxDepth(a) == 3
