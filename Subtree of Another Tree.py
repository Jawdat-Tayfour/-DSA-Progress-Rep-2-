#my solution ^_^ 

class TreeNode():
    def __init__(self,value=None,right=None,left=None):
        self.value = value
        self.right = right
        self.left = left 
"""def isSubtree(root1:TreeNode,root2:TreeNode) -> bool:
    if root1 is None and root2 is None:
        return True
    elif root1 is None or root2 is None:
        return False
    leftresult = False
    rightresult = False 
    if root1.value == root2.value:
            leftresult = isSubtree(root1.left,root2.left)
            rightresult = isSubtree(root1.right,root2.right)
                
    if leftresult and rightresult:
        return True        
    else:
        return isSubtree(root1.left, root2) or isSubtree(root1.right, root2)"""
# Time Complexity O(n * m), where 'n' is the total number of nodes in root1, and 'm' is the total number of nodes in root2.   
# 
# Neet Code Solution:
#  
def SubTree(S:TreeNode,T:TreeNode):
    if not T :
        return True 
    if not S :
        return False 
    if SameTree(S,T):
        return True 
    return SubTree(S.left,T)or SubTree(S.right,T)
def SameTree(S:TreeNode,T:TreeNode):
    if not S and not T :
        return True 
    if S and T and S.value == T.value:
        return (SameTree(S.left,T.left)and
                SameTree(S.right,T.right))
    return False 

#Time Complexity is also O(m*n) but more efficient
# because it avoids unnecessary recursive calls when it can determine that T is not a subtree of S based on certain conditions.
#  It reduces the number of traversals and short-circuits the process when possible. ^_^ have a good day fella.

# Tree 1: root1
#       1
#      / \
#     2   3
#    / \   \
#   4   5   6

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
root1.right.right = TreeNode(6)

# Tree 2: root2 (subtree of root1)
#     2
#    / \
#   4   5

root2 = TreeNode(2)
root2.left = TreeNode(4)
root2.right = TreeNode(5)
result = SubTree(root1, root2)
print(result)




