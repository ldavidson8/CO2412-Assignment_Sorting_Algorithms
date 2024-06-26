import random

NUM_OF_NAMES = 4000


# Read and trim a file to 4,000 lines
def read_and_trim_file(filename):
    with open(filename, "r") as file:
        lines = file.read().splitlines()[:NUM_OF_NAMES]
    return lines


first_names = read_and_trim_file("firstNames.txt")
last_names = read_and_trim_file("lastNames.txt")

# Generate a list of full names by combining random first and last names
full_names = [
    random.choice(first_names) + " " + random.choice(last_names)
    for _ in range(NUM_OF_NAMES)
]

with open("fullNames.txt", "w") as full_names_f:
    full_names_f.write("\n".join(full_names))

# Find and output the longest name in terms of characters
longest_name = max(full_names, key=len)
print(f"The longest name is: {longest_name}")

print("Full names have been written to 'fullNames.txt'.")
