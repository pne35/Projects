# Open the text file and read the numbers
with open("numbers.txt", "r") as file:
    # Read all lines, strip whitespace, and convert them to integers
    numbers = [int(line.strip()) for line in file]

# Calculate the sum of the numbers
total_sum = sum(numbers)

# Extract the first 10 digits of the sum
first_ten_digits = str(total_sum)[:10]

print("The first ten digits of the sum are:", first_ten_digits)
