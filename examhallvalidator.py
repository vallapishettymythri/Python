subject = input()
items = input().split()

allowed = True

for item in items:
    if item == "pen" or item == "pencil":
        continue
    elif item == "calculator":
        if subject != "Math":
            allowed = False
            break
    else:
        allowed = False
        break

if allowed:
    print("Allowed")
else:
    print("Confiscate")
