# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result=[]
        current_lvl=deque([root])
        while current_lvl:
            count=len(current_lvl)
            temp=[]

            for _ in range(count):
                node=current_lvl.popleft()
                temp.append(node.val)

                if node.left:
                    current_lvl.append(node.left)
                if node.right:
                    current_lvl.append(node.right)

            result.append(temp)

        return result
