from collections import Counter

def find_duplicates(input_list):
    counter = Counter(input_list)
    duplicates = []
    for item, count in counter.items():
        if count > 1:
            duplicates.extend([item] * (count - 1))
    return duplicates

# Example usage
my_list = [0,0,0,0,0,0,0,0]
duplicates = find_duplicates(my_list)
print(duplicates)  # Output: [1, 2, 2, 3]
