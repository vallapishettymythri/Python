#Day-to-Activity Planner
n=input()
match n:
    case "Monday":
        print("Go for a run")
    case "Tuesday":
        print("Attend a cooking class")
    case "Wednesday":
        print("Work on a personal project")
    case "Thursday":
        print("Watch a movie")
    case "Friday":
        print("Hang out with friends")
    case "Saturday":
        print("Go shopping")
    case "Sunday":
        print("Relax at home")
    case _: 
        print("Invalid day input.")
