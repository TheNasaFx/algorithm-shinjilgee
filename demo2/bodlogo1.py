from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def calculate_depth(root):
    if not root:
        return 0  # If the tree is empty, the depth is 0
    
    queue = deque([root])
    depth = 0
    
    while queue:
        depth += 1
        level_size = len(queue)
        
        for _ in range(level_size):
            node = queue.popleft()  # Dequeue the front node
            
            if node.left:
                queue.append(node.left)  # Enqueue left child
            if node.right:
                queue.append(node.right)  # Enqueue right child
    
    return depth

# test case like this :root = [3,9,20,null,null,15,7] 
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

depth = calculate_depth(root)
print(depth)