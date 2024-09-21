#Prompt users input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
#Customize the reminder
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task "
    case "medium":
        reminder = f"'{task}' is a medium priority task "
    case "low":
        reminder = f"'{task}' is a low priority task. "
    case _:
        reminder = ("invalid priority level")
#Consider if task is time-bound
if time_bound == "yes":
    reminder = reminder + "that requires immediate attention today!"
elif time_bound == "no":
    reminder = reminder + "Consider completing it when you have free time."
print(f"Reminder: {reminder}")  