# Step 1: Take user input and write it to output.txt
user_input = input("Enter some text to write to the file: ")

# Open the file in write mode to write the user input to it
with open('output.txt', 'w') as file:
    file.write(user_input + '\n')  # Add newline after the input

# Step 2: Append additional data to the same file
additional_data = input("Enter additional text to append to the file: ")

# Open the file in append mode to add data without overwriting
with open('output.txt', 'a') as file:
    file.write(additional_data + '\n')  # Add newline after the additional input

# Step 3: Read and display the final content of the file
print("\nFinal content of the file 'output.txt':")
with open('output.txt', 'r') as file:
    content = file.read()
    print(content)
