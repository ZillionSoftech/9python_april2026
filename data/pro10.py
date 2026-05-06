delhi = int(input("Enter Delhi team score : "))
jaipur = int(input("Enter Jaipur team score : "))
rewari = int(input("Enter Rewari team score : "))
gurugram = int(input("Enter Gurugram team score : "))


if delhi > jaipur:
    if delhi > rewari:
        if delhi>gurugram:
            print(f"Delhi is winner : {delhi}")
        else:
            print(f"Gurugram is winner : {gurugram}")
    else:
        if rewari>gurugram:
            print(f"Rewari is winner : {rewari}")
        else:
            print(f"Gurugram is winner : {gurugram}")
else:
    if jaipur>rewari:
        if jaipur>gurugram:
            print(f"Jaipur is winner : {jaipur}")
        else:
            print(f"Gurugram is winner : {gurugram}")
    else:
        if rewari>gurugram:
            print(f"Rewari is winner : {rewari}")
        else:
            print(f"Gurugram is winner : {gurugram}")