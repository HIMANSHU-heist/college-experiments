tasks = []

# Adding tasks
n = int(input("How many tasks? "))
for i in range(n):
    t = input(f"Enter task {i+1}: ")
    tasks.append(t)

print("Current Tasks:", tasks)

# Removing a task
rem = input("Enter task to remove: ")
if rem in tasks:
    tasks.remove(rem)

# Sorting tasks
tasks.sort()

# Updating a task
idx = int(input("Enter index to update (0, 1...): "))
tasks[idx] = input("Enter new task: ")

# Final Tuple
final_tasks = tuple(tasks)
print("Final Tasks (Tuple):", final_tasks)