class TreeNode {
    constructor(val = 0, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

function sortedArrayToBST(nums) {
    if (!nums.length) return null;

    function convertToBST(left, right) {
        if (left > right) return null;

        const mid = Math.floor((left + right) / 2);
        const node = new TreeNode(nums[mid]);

        node.left = convertToBST(left, mid - 1);
        node.right = convertToBST(mid + 1, right);

        return node;
    }

    return convertToBST(0, nums.length - 1);
}

// Example usage
const nums1 = [-10, -3, 0, 5, 9];
const nums2 = [1, 3];
console.log(sortedArrayToBST(nums1));  // Output: TreeNode representing the BST
console.log(sortedArrayToBST(nums2));  // Output: TreeNode representing the BST
