# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result=0

        def getHeight(root):

            if not root:
                return 0

            left=getHeight(root.left)
            right=getHeight(root.right)

            self.result=max(self.result,left+right)

            return 1+max(left,right)

        getHeight(root)
        return self.result