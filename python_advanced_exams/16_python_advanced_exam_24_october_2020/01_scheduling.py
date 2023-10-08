jobs = [int(x) for x in input().split(", ")]
idx = int(input())

computed_element = jobs[idx]
total_cycles = 0
for job in sorted(jobs):
    if job > computed_element:
        break
    total_cycles += job

print(total_cycles)
