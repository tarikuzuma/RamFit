def convert_to_cm(feet, inches):
    total_inches = feet * 12 + inches
    cm = total_inches * 2.54
    return cm

# Get input from the user
feet = int(input("Enter the feet value: "))
inches = int(input("Enter the inches value: "))

# Convert to centimeters
result = convert_to_cm(feet, inches)

# Display the result
print("The equivalent length is", result, "cm.")
