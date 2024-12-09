class StackWithBackup:
    def __init__(self, k):
        self.stack = []
        self.k = k
        self.operation_count = 0
        self.total_cost = 0

    def push(self, item):
        self.stack.append(item)
        self.operation_count += 1
        self.total_cost += 1  

        if self.operation_count % self.k == 0:
            self.backup()

    def pop(self):
        if not self.stack:
            print("Stack is empty.")
            return None
        self.stack.pop()
        self.operation_count += 1
        self.total_cost += 1  

        if self.operation_count % self.k == 0:
            self.backup()

    def backup(self):
        self.total_cost += self.k  
        backup_stack = self.stack.copy()
        print("Backup completed:", backup_stack)

    def get_amortized_cost(self):
        return self.total_cost / self.operation_count if self.operation_count != 0 else 0

k = 5  
stack = StackWithBackup(k)
n = 20  

for i in range(1, n + 1):
    if i % 2 == 0:
        stack.pop()
    else:
        stack.push(i)

print(f"Total cost after {n} operations: {stack.total_cost}")
print(f"Amortized cost per operation: {stack.get_amortized_cost()}")
