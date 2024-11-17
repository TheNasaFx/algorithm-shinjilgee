def knapsack(w, weights, values, n):
    dp = [[0 for _ in range(w + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(values[i - 1] + dp[i - 1][j - weights[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][w]

if __name__ == "__main__":
    weights = [1, 2, 3]
    values = [10, 15, 40]
    max_weight = 6
    n = len(values)
    print(f"Maximum value in Knapsack = {knapsack(max_weight, weights, values, n)}")
