#  binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        
        # middle element
        mid = len(nums) // 2
        
        # Create a tree node with the middle element as the root
        root = TreeNode(nums[mid])
        
        root.left = self.sortedArrayToBST(nums[:mid])
        
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root

from collections import deque

def print_bst_level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    while result and result[-1] is None:
        result.pop()
    
    return result

# Example usage:
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    nums1 = [-10, -3, 0, 5, 9]
    bst1 = sol.sortedArrayToBST(nums1)
    print("BST for nums1:", print_bst_level_order(bst1))  # Output: [0, -3, 9, -10, None, 5]

    # Example 2
    nums2 = [1, 3]
    bst2 = sol.sortedArrayToBST(nums2)
    print("BST for nums2:", print_bst_level_order(bst2))  # Output: [3, 1] or [1, None, 3]
