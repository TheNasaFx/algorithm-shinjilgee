def file_hevleh():
    filename = "example.txt"
    
    try:
        with open(filename, 'r') as file:
            content = file.read().strip()
        
        raw_data_str, sorted_data_str = content.split(' | ')
        raw_data_str = raw_data_str.strip('[]')
        sorted_data_str = sorted_data_str.strip('[]')
        
        raw_data = list(map(int, raw_data_str.split()))
        sorted_data = list(map(int, sorted_data_str.split()))
        
        return raw_data, sorted_data
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return [], []
    except ValueError:
        print("Error in converting file content to integers.")
        return [], []


def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left_half = merge_sort(nums[:mid])
    right_half = merge_sort(nums[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

def binary_search(nums, low, high, target):
    if low > high:
        return -1

    mid = low + (high - low) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return binary_search(nums, low, mid - 1, target)
    else:
        return binary_search(nums, mid + 1, high, target)

def find_max(nums, low, high):
    if low == high:
        return nums[low]

    mid = low + (high - low) // 2

    max_left = find_max(nums, low, mid)
    max_right = find_max(nums, mid + 1, high)

    return max(max_left, max_right)

def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums
