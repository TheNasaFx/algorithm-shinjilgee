def find_three_numbers_with_sum(arr, target_sum):
    # Sort the array
    arr.sort()
    n = len(arr)
    results = []  # To store the valid combinations

    # Iterate through each number in the array
    for i in range(n):
        first_number = arr[i]
        left = i  # Start from the current index (to allow duplicates)
        right = n - 1  # Start from the end of the array

        # Use two pointers to find the other two numbers
        while left <= right:
            current_sum = first_number + arr[left] + arr[right]

            if current_sum == target_sum:
                results.append((first_number, arr[left], arr[right]))  # Found the combination
                left += 1  # Move left pointer to find more combinations
                right -= 1  # Move right pointer to find more combinations
            elif current_sum < target_sum:
                left += 1  # Move left pointer to the right
            else:
                right -= 1  # Move right pointer to the left

    return results if results else "No combination found"  # Return combinations or no result

# Example usage
arr = [11, 2, 5, 7, 3]
target_sum = 21
result = find_three_numbers_with_sum(arr, target_sum)
print(result)  # Output could include (3, 7, 11) and (5, 5, 11)
