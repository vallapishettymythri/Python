#1)match- Instead of writing many if-else, the match stmt selects one of the many code blocks to be executed.
day=4
match day:
    case 1: 
        print("monday")
    case 2: 
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6: 
        print("saturday")
    case 7: 
        print("sunday")


#2)Default value: For default value when the code doesnt match we use _ (underscore) to print when they are no other matches.
day=4
match day:
    case 6: 
        print("saturday")
    case 7: 
        print("sunday")
    case _:
        print("weekday")

#3)Combine values: use pipe character "|" an or operator to evaluate to check for more than one value.
day=4
match day:
    case 1|2|3|4|5:
        print("Weekday")
    case 6|7:
        print("Weekend")


#4)If statements as guards: Extra contion check
month=5
day=4
match day:
    case 1|2|3|4|5 if month==5:
        print("weekday")
    case 1|2|3|4|5 if month==5:
        print("Weekend")
    case _:
        print("No match")
