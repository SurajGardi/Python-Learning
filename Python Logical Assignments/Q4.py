# 4. Find given number is palindrome. The output will be True if it’s a Palindrome number otherwise it would be False.

num = 121
temp = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if temp == rev:
    print("True")
else:
    print("False")