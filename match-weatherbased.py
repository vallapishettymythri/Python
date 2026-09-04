#Weather-Based Dressing Advisor using Match-Case
weather=input()
match weather:
    case "hot":
        print("Wear light clothes")
    case "cold":
        print("Wear a jacket")
    case "rainy":
        print("Carry an umbrella")