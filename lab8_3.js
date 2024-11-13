function assignBikes(students, bikes) {
    const distances = [];
    const result = new Array(students.length).fill(-1);
    const bike_used = new Array(bikes.length).fill(false);

    for (let i = 0; i < students.length; i++) {
        for (let j = 0; j < bikes.length; j++) {
            const dist = Math.abs(students[i][0] - bikes[j][0]) + Math.abs(students[i][1] - bikes[j][1]);
            distances.push([dist, i, j]);
        }
    }

    distances.sort((a, b) => a[0] - b[0]);

    for (const [dist, student, bike] of distances) {
        if (result[student] === -1 && !bike_used[bike]) {
            result[student] = bike;
            bike_used[bike] = true;
        }
    }

    return result;
}

// Unit test
const assert = require('assert');
assert.deepStrictEqual(assignBikes([[0, 0], [1, 1]], [[0, 1], [4, 3], [2, 1]]), [0, 2]);
assert.deepStrictEqual(assignBikes([[0, 0]], [[0, 1]]), [0]);
assert.deepStrictEqual(assignBikes([[0, 0], [2, 2]], [[1, 1], [3, 3]]), [0, 1]);

console.log("All tests passed!");
