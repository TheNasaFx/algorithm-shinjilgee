def calculate_completion_time(programs, num_cpus, processes_per_cpu):
    programs.sort(reverse=True)
    
    cpus = [0] * num_cpus
    
    for i, program_time in enumerate(programs):
        cpu_index = i % num_cpus
        cpus[cpu_index] += program_time
    
    overall_completion_time = max(cpus)
    return overall_completion_time

def main():
    programs = [10, 15, 30]  # P0, P1, P2
    
    num_cpus = 3
    processes_per_cpu = 2
    
    completion_time = calculate_completion_time(programs, num_cpus, processes_per_cpu)
    print(f"Overall completion time for all programs: {completion_time} ms")

if __name__ == "__main__":
    main()
