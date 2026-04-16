# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        q = collections.deque([root])

        while q:
            rightSide = None
            # The current level we are in
            qLen = len(q)

            #Run through that entire level
            for i in range(qLen):
                #Pop elements from the left hand side
                node = q.popleft()
                #If the node is not null we are left with last right
                #side value of that level
                if node:
                    rightSide = node
                    #Adding the children of the right side's node
                    q.append(node.left)
                    q.append(node.right)

            if rightSide:
                res.append(rightSide.val)

        return res

            





        