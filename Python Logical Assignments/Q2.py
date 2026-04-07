# 2. Star Patterns

# (a) Pyramid

for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

# --------------------------------

# (b) Increasing Triangle

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

# --------------------------------

# (c) Decreasing Triangle

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

