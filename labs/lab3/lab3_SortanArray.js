function sortArray(nums) {
    quickSort(nums, 0, nums.length - 1);
    return nums;
}

function quickSort(arr, low, high) {
    const stack = [];
    stack.push({ low, high });

    while (stack.length) {
        const { low, high } = stack.pop();
        if (low < high) {
            const pi = partition(arr, low, high);
            stack.push({ low, high: pi - 1 });
            stack.push({ low: pi + 1, high });
        }
    }
}

function partition(arr, low, high) {
    const pivot = medianOfThree(arr, low, high);
    let i = low - 1;
    for (let j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            [arr[i], arr[j]] = [arr[j], arr[i]];
        }
    }
    [arr[i + 1], arr[high]] = [arr[high], arr[i + 1]];
    return i + 1;
}

function medianOfThree(arr, low, high) {
    const mid = Math.floor((low + high) / 2);
    if (arr[low] > arr[mid]) [arr[low], arr[mid]] = [arr[mid], arr[low]];
    if (arr[low] > arr[high]) [arr[low], arr[high]] = [arr[high], arr[low]];
    if (arr[mid] > arr[high]) [arr[mid], arr[high]] = [arr[high], arr[mid]];
    [arr[mid], arr[high]] = [arr[high], arr[mid]];
    return arr[high];
}

// Example usage
const nums1 = [5, 2, 3, 1];
const nums2 = [5, 1, 1, 2, 0, 0];
console.log(sortArray(nums1));  // Output: [1, 2, 3, 5]
console.log(sortArray(nums2));  // Output: [0, 0, 1, 1, 2, 5]
