feedback=input()
match feedback:
    case "A":
        print("Excellent!")
    case "B":
        print("Good job!")
    case "c":
        print("You can do better.")
    case "D":
        print("Needs improvement.")
    case "E":
        print("Failed.")
    case _:
        print("Invalid grade input.")