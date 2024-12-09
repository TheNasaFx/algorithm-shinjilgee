from collections import deque

class Solution:
    def openLock(self, deadends, target):
        dead_set = set(deadends)
        visited = set()
        queue = deque([("0000", 0)])  # (current combination, steps)
        
        if "0000" in dead_set:
            return -1

        while queue:
            combination, steps = queue.popleft()

            if combination == target:
                return steps
            
            if combination in visited or combination in dead_set:
                continue
            
            visited.add(combination)
            
            # Generate all possible next states
            for i in range(4):
                digit = int(combination[i])
                for move in (-1, 1):  # Move the wheel up or down
                    new_digit = (digit + move) % 10
                    new_combination = combination[:i] + str(new_digit) + combination[i+1:]
                    if new_combination not in visited and new_combination not in dead_set:
                        queue.append((new_combination, steps + 1))
        
        return -1
