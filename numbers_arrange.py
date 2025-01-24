"""def move_zeros_to_end(numbers):
    non_zero_numbers = []
    for num in numbers:
        if num != 0:
            non_zero_numbers.append(num)
    
    # Count the number of zeros in the original list
    zero_count = numbers.count(0)
    
    # Add the zeros at the end of the non-zero numbers
    return non_zero_numbers + [0] * zero_count

# Example usage:
numbers = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]

print("Original list:")
print(numbers)

# Call the function to move zeros to the end
result = move_zeros_to_end(numbers)

print("\nMove all zero digits to end of the list:")
print(result)
"""
def arrange(number):
    non_zero=[]
    for num in number:
        if num!=0:
            non_zero.append(num)

    zero=number.count(0)

    return non_zero+[0]*zero

numbers = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
result=arrange(numbers)
print(result)