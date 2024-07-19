numbers = [3, 5, 7, 2, 8, 1, 9, 4, 6]

# Step 1: Find the maximum value
max_value = max(numbers)

# Step 2: Find the index of the maximum value
max_index = numbers.index(max_value)

# Step 3: Split the list into two parts
list1 = numbers[:max_index + 1]  # Up to and including the maximum value
list2 = numbers[max_index + 1:]  # All elements after the maximum value

print("List 1:", list1)
print("List 2:", list2)
