#Movie Ticket Price Calculator
customer = input()

match customer:
    case "Adult":
        print("Ticket Price: $15")
    case "child":
        print("Ticket Price: $8")
    case "Senior":
        print("Ticket Price: $10")
    case _:
        print("Invalid customer type.")

