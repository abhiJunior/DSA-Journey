# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = 0
        self.arr_path = [0]*10
    def pseudoPalindromicPaths (self, root: TreeNode | None) -> int:
        self.path(root)
        return self.result
         
    def path(self, root):
        if (root == None):
            return 0

        self.arr_path[root.val] += 1

        if root.left == None and root.right == None:
            ## logic for checking the pallindrome 
            odd_count = 0 
            for values in self.arr_path:
                if values % 2 == 1:
                    odd_count += 1
                
            if odd_count <= 1:
                self.result += 1
            
        left = self.path(root.left)
        right = self.path(root.right)
        self.arr_path[root.val] -= 1
        
        