#Library Late Fine Calculator
days_late = int(input())
is_member = input()

if days_late <= 0:
    print("No Fine")
else:
    if days_late <= 7:
        fine = days_late * 10
    elif days_late <= 14:
        fine = days_late * 20
    else:
        fine = days_late * 50

    if is_member == "True":
        fine = fine * 50 // 100

    print("Fine: ₹" + str(fine))