const assert = require('assert');
const { fileHevleh, mergeSort, insertionSort, binarySearch, findMax } = require('./algo');

describe('algo', function() {
    let rawData, sortedData;

    before(function() {
        [rawData, sortedData] = fileHevleh();
    });

    it('should read and parse the file correctly', function() {
        console.log('Raw Data:', rawData);
        console.log('Sorted Data:', sortedData);
        assert.deepStrictEqual(rawData, [3, 5, 7, 9, 2, 4, 6, 8, 1, 0]);
        assert.deepStrictEqual(sortedData, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);
    });

    it('should sort the array using merge sort', function() {
        const sortedNums = mergeSort(rawData);
        console.log('Merge Sorted Data:', sortedNums);
        assert.deepStrictEqual(sortedNums, sortedData);
    });

    it('should sort the array using insertion sort', function() {
        const sortedNums = insertionSort([...rawData]);
        console.log('Insertion Sorted Data:', sortedNums);
        assert.deepStrictEqual(sortedNums, sortedData);
    });

    it('should find the target using binary search', function() {
        const target = 7;
        const sortedNums = mergeSort(rawData);
        const index = binarySearch(sortedNums, 0, sortedNums.length - 1, target);
        console.log(`Binary Search for ${target}: Index ${index}`);
        assert.strictEqual(index, sortedNums.indexOf(target));
    });

    it('should return -1 when target is not found using binary search', function() {
        const target = 10;
        const sortedNums = mergeSort(rawData);
        const index = binarySearch(sortedNums, 0, sortedNums.length - 1, target);
        console.log(`Binary Search for ${target}: Index ${index}`);
        assert.strictEqual(index, -1);
    });

    it('should find the maximum value in the array', function() {
        const maxNum = findMax(rawData, 0, rawData.length - 1);
        console.log('Maximum Value:', maxNum);
        assert.strictEqual(maxNum, Math.max(...rawData));
    });
});
