delhi = int(input("Enter Delhi team score : "))
jaipur = int(input("Enter Jaipur team score : "))
rewari = int(input("Enter Rewari team score : "))


if delhi > jaipur:
    if delhi > rewari:
        print(f"Delhi is winner : {delhi}")
    else:
        print(f"Rewari is winner : {rewari}")
else:
    if jaipur>rewari:
        print(f"Jaipur is winner : {jaipur}")
    else:
        print(f"Rewari is winner : {rewari}")