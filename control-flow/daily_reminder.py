# daily_reminder.py

# Prompt the user for a single task
task = input("Enter your task description: ")
task_priority = input("Choose task priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

# Use match-case to handle priority
match task_priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:  # default/fallback
        reminder = f"'{task}' has an unspecified priority"

# Modify reminder based on time sensitivity
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Print the final reminder
print("\nReminder:", reminder)

