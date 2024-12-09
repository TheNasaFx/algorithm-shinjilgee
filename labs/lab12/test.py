from collections import deque

class Solution:
    def openLock(self, deadends, target):
        dead = set(deadends) 
        if "0000" in dead:
            return -1  
        
        queue = deque([("0000", 0)])  
        visited = set("0000")  
        
        while queue:
            current, turns = queue.popleft()
            
            if current == target:
                return turns
            
            for i in range(4):  
                digit = int(current[i])
                for move in [-1, 1]:  
                    next_digit = (digit + move) % 10
                    next_combination = current[:i] + str(next_digit) + current[i+1:]
                    
                    if next_combination not in visited and next_combination not in dead:
                        visited.add(next_combination)
                        queue.append((next_combination, turns + 1))
        
        return -1  

solution = Solution()
print(solution.openLock(["0201", "0101", "0102", "1212", "2002"], "0202"))  # Output: 6
print(solution.openLock(["8888"], "0009"))  # Output: 1
print(solution.openLock(["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888"))  # Output: -1
