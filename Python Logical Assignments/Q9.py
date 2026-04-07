# 9. Sort Dictionary by Keys (Manual)

myDict = {'Ashwin': 100, 'rakesh': 9, 'Ravindra': 25, 'yash': 200, 'sai': 32}

keys = list(myDict.keys())

# Bubble Sort on keys
for i in range(len(keys)):
    for j in range(0, len(keys)-i-1):
        if keys[j] > keys[j+1]:
            temp = keys[j]
            keys[j] = keys[j+1]
            keys[j+1] = temp

sorted_dict = {}
for key in keys:
    sorted_dict[key] = myDict[key]

print(sorted_dict)