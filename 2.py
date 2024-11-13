import time
from collections import deque

class Process:
    def __init__(self, name, burst_time):
        self.name = name
        self.burst_time = burst_time

    def __str__(self):
        return f"Process({self.name}, {self.burst_time})"

def round_robin_scheduling(processes, time_quantum):
    queue = deque(processes)
    current_time = 0

    while queue:
        process = queue.popleft()
        print(f"Current Time: {current_time} - Running {process.name}")
        
        if process.burst_time > time_quantum:
            process.burst_time -= time_quantum
            current_time += time_quantum
            queue.append(process)
        else:
            current_time += process.burst_time
            process.burst_time = 0
            print(f"Current Time: {current_time} - Finished {process.name}")

def main():
    # Define processes with their burst times
    processes = [
        Process("Process1", 10),
        Process("Process2", 5),
        Process("Process3", 8),
        Process("Process4", 12)
    ]

    # Define time quantum for round-robin scheduling
    time_quantum = 4

    print("Starting Round-Robin Scheduling Simulation...")
    round_robin_scheduling(processes, time_quantum)
    print("Scheduling Simulation Complete.")

if __name__ == "__main__":
    main()
