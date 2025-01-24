"""
4. Write a Python program to move all zero digits to the end of a given list of
numbers.
Expected output:
Original list:
[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
Move all zero digits to end of the said list of numbers:

[3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
"""

num=[3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print("original number")
print(num)

non_zero=[]

for i in num:
    if i!=0:
        non_zero.append(i)

zero=num.count(0)

result=non_zero+[0]*zero

print(result)