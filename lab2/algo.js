const fs = require('fs');

function fileHevleh() {
    const filename = 'example.txt';

    try {
        const content = fs.readFileSync(filename, 'utf8').trim();
        const [rawDataStr, sortedDataStr] = content.split(' | ');
        const rawData = rawDataStr.replace('[', '').replace(']', '').split(' ').map(Number);
        const sortedData = sortedDataStr.replace('[', '').replace(']', '').split(' ').map(Number);

        return [rawData, sortedData];
    } catch (err) {
        if (err.code === 'ENOENT') {
            console.error(`File '${filename}' not found.`);
        } else {
            console.error('Error in converting file content to integers.');
        }
        return [[], []];
    }
}

function mergeSort(nums) {
    if (nums.length <= 1) {
        return nums;
    }

    const mid = Math.floor(nums.length / 2);
    const leftHalf = mergeSort(nums.slice(0, mid));
    const rightHalf = mergeSort(nums.slice(mid));

    return merge(leftHalf, rightHalf);
}

function merge(left, right) {
    const sortedList = [];
    let i = 0, j = 0;

    while (i < left.length && j < right.length) {
        if (left[i] <= right[j]) {
            sortedList.push(left[i]);
            i++;
        } else {
            sortedList.push(right[j]);
            j++;
        }
    }

    return sortedList.concat(left.slice(i)).concat(right.slice(j));
}

function binarySearch(nums, low, high, target) {
    if (low > high) {
        return -1;
    }

    const mid = Math.floor(low + (high - low) / 2);

    if (nums[mid] === target) {
        return mid;
    } else if (nums[mid] > target) {
        return binarySearch(nums, low, mid - 1, target);
    } else {
        return binarySearch(nums, mid + 1, high, target);
    }
}

function findMax(nums, low, high) {
    if (low === high) {
        return nums[low];
    }

    const mid = Math.floor(low + (high - low) / 2);

    const maxLeft = findMax(nums, low, mid);
    const maxRight = findMax(nums, mid + 1, high);

    return Math.max(maxLeft, maxRight);
}

function insertionSort(nums) {
    for (let i = 1; i < nums.length; i++) {
        const key = nums[i];
        let j = i - 1;
        while (j >= 0 && nums[j] > key) {
            nums[j + 1] = nums[j];
            j--;
        }
        nums[j + 1] = key;
    }
    return nums;
}

module.exports = { fileHevleh, mergeSort, insertionSort, binarySearch, findMax };
