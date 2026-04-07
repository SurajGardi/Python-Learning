# 1. Create 2 separate arrays for even and odd numbers within the range of 0 to 100.

even = []
odd = []

for i in range(0, 101):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even Numbers:", even)
print("Odd Numbers:", odd)