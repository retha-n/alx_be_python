task = str(input("Enter yoyr task:"))
priority = str(input("Priority (high/medium/low):"))
time_bound = str(input("Is it time-bound? (yes/no):"))

match priority:
    case "high" if time_bound == "yes":
        print(f"'{task}' is a {priority} priority task that requires immediate attention today!")
    case "medium" if time_bound == "yes":
        print(f"'{task}' is a {priority} priority task that requires immediate attention today!")
    case "low" if time_bound == "yes":
        print(f"'{task}' is a {priority} priority task that requires immediate attention today!")
    case "high" if time_bound != "yes":
        print(f"'{task}' is a {priority} priority task. Consider completing it when you have free time.")
    case "medium" if time_bound != "yes":
        print(f"'{task}' is a {priority} priority task. Consider completing it when you have free time.")
    case "low" if time_bound != "yes":
        print(f"'{task}' is a {priority} priority task. Consider completing it when you have free time.")