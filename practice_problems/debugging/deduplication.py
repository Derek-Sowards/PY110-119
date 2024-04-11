data = [1, 2, 3, 2, 4, 3]
unique_data = []
# The order is not guaranteed to be [1, 2, 3, 4]


seen = set()
for element in data:
    if element not in seen:
        seen.add(element)
        unique_data.append(element)

print(unique_data)