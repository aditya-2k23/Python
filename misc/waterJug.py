def water(j1, j2, c1, c2):
    transfer = min(j1, c2 - j2)
    j1 -= transfer
    j2 += transfer
    return j1, j2

def water_jug():
    c1 = int(input("Enter the capacity of the first jug: "))
    c2 = int(input("Enter the capacity of the second jug: "))
    goal = int(input("Enter the goal amount of water: "))

    j1, j2 = 0, 0
    steps = [(j1, j2)]

    while True:
        if j1 == goal or j2 == goal:
            break
        elif j1 == 0:
            j1 = c1
        elif j2 == c2:
            j2 = 0
        else:
            j1, j2 = water(j1, j2, c1, c2)
            steps.append((j1, j2))

    print("Solution:")
    for step in steps:
        print(step)

water_jug()
