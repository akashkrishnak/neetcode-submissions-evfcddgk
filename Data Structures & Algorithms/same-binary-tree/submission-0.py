# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.v1=[]
        def traverse(root):
            if not root:
                self.v1.append('null')
                return
            
            self.v1.append(root.val)
            traverse(root.left)
            traverse(root.right)

        traverse(p)
        a=[x for x in self.v1]
        self.v1=[]
        traverse(q)
        b=[x for x in self.v1]
        if a==b:
            return True
        else:
            return False
