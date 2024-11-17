class Solution {
    numTrees(n) {
        const dp = new Array(n + 1).fill(0);

        dp[0] = 1; 
        dp[1] = 1; 

        for (let nodes = 2; nodes <= n; nodes++) {
            for (let root = 1; root <= nodes; root++) {
                const leftTrees = dp[root - 1]; 
                const rightTrees = dp[nodes - root]; 
                dp[nodes] += leftTrees * rightTrees;
            }
        }

        return dp[n];
    }
}

const solution = new Solution(); 
let ret = solution.numTrees(3);  
console.log(ret);  

ret = solution.numTrees(1);
console.log(ret);  
