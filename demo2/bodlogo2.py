class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root):
    def check_height(node):
        if not node:
            return 0  # Null tree has height 0
        
        left_height = check_height(node.left)
        if left_height == -1:
            return -1  # Left subtree is not balanced
        
        right_height = check_height(node.right)
        if right_height == -1:
            return -1  # Right subtree is not balanced
        
        if abs(left_height - right_height) > 1:
            return -1  # Current node is not balanced
        
        return max(left_height, right_height) + 1  # Height of current node
    
    return check_height(root) != -1

#test cases
root = TreeNode(13)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(is_balanced(root)) 