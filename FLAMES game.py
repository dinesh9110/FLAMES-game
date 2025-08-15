def remove_common_letters(name1, name2):
    # Convert names to lowercase
    name1 = name1.lower().strip()
    name2 = name2.lower().strip()

    # Remove common letters
    for letter in name1:
        if letter in name2:
            name1 = name1.replace(letter, '', 1)
            name2 = name2.replace(letter, '', 1)

    # Return the total length of remaining letters
    return len(name1 + name2)


def flames_result(count):
    flames = ['Friends', 'Lovers', 'Affectionate', 'Marriage', 'Enemies', 'Siblings']

    while len(flames) > 1:
        split_index = (count % len(flames)) - 1

        if split_index >= 0:
            right = flames[split_index + 1:]
            left = flames[:split_index]
            flames = right + left
        else:
            flames = flames[:len(flames) - 1]

    return flames[0]


# Input names
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

# Get the remaining letters after removing common ones
count = remove_common_letters(name1, name2)

# Get the FLAMES result
result = flames_result(count)

# Display the result
print(f"The relationship between {name1} and {name2} is: {result}")
