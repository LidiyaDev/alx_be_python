# daily_reminder.py

# Prompt the user for a task description
task = input("Enter your task: ")

# Prompt the user for the task's priority
priority = input("Priority (high/medium/low): ").lower()

# Prompt the user to check if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority and time sensitivity using match case and if statement
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task."
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task."
    case "low":
        reminder = f"Note: '{task}' is a low priority task."

if time_bound == "yes":
    reminder += " It requires immediate attention today!"

# Print the customized reminder
print(reminder)
