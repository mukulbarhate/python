# import random
# import string

# # Function to generate a random string of specified length
# def generate_random_string(length):
#     characters = string.ascii_letters.lower() 
#     return ''.join(random.choice(characters) for _ in range(length))

# # Usage example
# for i in range(7):
#     random_string = generate_random_string(i)
# print(random_string)

import random

# List of names
names = ["Mandar","Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"]

# Function to check probability of printing a name within a range of 6
def check_probability():
    # Generate a random index within the range of 6
    index = random.randint(0, 5)
    # Get the name at the generated index
    selected_name = names[index]
    return selected_name

# Number of iterations
iterations = 10000

# Counter for each name
name_count = {name: 0 for name in names}

# Perform iterations and count occurrences of each name
for _ in range(iterations):
    name = check_probability()
    name_count[name] += 1

# Calculate probabilities
probabilities = {name: count / iterations for name, count in name_count.items()}

# Print probabilities
for name, probability in probabilities.items():
    print(f"Name: {name}, Probability: {probability:.2f}")
