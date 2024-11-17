function optimal_bst(keys, f, n) {
    let cost = Array.from({ length: n }, () => Array(n).fill(0));

    for (let i = 0; i < n; i++) {
        cost[i][i] = f[i];
    }

    for (let length = 2; length <= n; length++) {
        for (let i = 0; i < n - length + 1; i++) {
            let j = i + length - 1;
            cost[i][j] = Infinity;
            let f_sum = f.slice(i, j + 1).reduce((a, b) => a + b, 0);
            
            for (let r = i; r <= j; r++) {
                let left_cost = r > i ? cost[i][r - 1] : 0;
                let right_cost = r < j ? cost[r + 1][j] : 0;
                let total_cost = left_cost + right_cost + f_sum;
                cost[i][j] = Math.min(cost[i][j], total_cost);
            }
        }
    }

    return cost[0][n - 1];
}

const keys1 = [5, 6];
const f1 = [17, 25];
const n1 = keys1.length;
const min_cost1 = optimal_bst(keys1, f1, n1);
console.log(`Minimum search cost: ${min_cost1}`);  

const keys2 = [10, 12, 20];
const f2 = [34, 8, 50];
const n2 = keys2.length;
const min_cost2 = optimal_bst(keys2, f2, n2);
console.log(`Minimum search cost: ${min_cost2}`);  

const keys3 = [10, 12];
const f3 = [10, 20];
const n3 = keys3.length;
const min_cost3 = optimal_bst(keys3, f3, n3);
console.log(`Minimum search cost: ${min_cost3}`);  
