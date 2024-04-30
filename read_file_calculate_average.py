# Path to the file
file_path = 'C:\\Users\\Owner\\PycharmProjects\\100-days-python\\IDDQ.txt'

# Initialize sum and count variables for calculating the average
total_sum = 0
count = 0

# Open the file and read line by line
with open(file_path, 'r') as file:
    for line in file:
        # Check if the line starts with "IDDQ ="
        if line.strip().startswith('IDDQ ='):
            # Try to split the line at '=' and convert the second part to float
            parts = line.split('=')
            if len(parts) == 2:  # Ensure there are two parts
                try:
                    # Attempt to convert the second part to a float
                    number = float(parts[1].strip())
                    # If successful, add the number to total_sum and increment count
                    total_sum += number
                    count += 1
                except ValueError:
                    # If conversion to float fails, ignore this line
                    continue

# Calculate and print the average if any numbers were found
if count > 0:
    average = total_sum / count
    print(f"The average of numbers after 'IDDQ =' is: {average}")
else:
    print("No valid 'IDDQ =' numbers found in the file.")
