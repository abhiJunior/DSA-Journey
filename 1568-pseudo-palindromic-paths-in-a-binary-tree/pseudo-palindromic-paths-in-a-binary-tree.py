class Solution:
    def __init__(self):
        self.result = 0

    def pseudoPalindromicPaths(self, root: TreeNode | None) -> int:
        self.result = 0  # reset in case the object is reused
        self.path(root, 0)
        return self.result

    def path(self, root, mask):
        if root is None:
            return

        mask ^= 1 << root.val

        if root.left is None and root.right is None:
            if mask & (mask - 1) == 0:
                self.result += 1
            return

        self.path(root.left, mask)
        self.path(root.right, mask)