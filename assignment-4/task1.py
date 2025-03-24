# Task 1: Read a File and Handle Errors
try:
    # Attempt to open the file in read mode
    with open('sample.txt', 'r') as file:
        # Read and print the content line by line
        for line in file:
            print(line.strip())  # Strip any extra newlines or spaces
except FileNotFoundError:
    # Handle the case where the file does not exist
    print("Error: The file 'sample.txt' does not exist.")
except Exception as e:
    # Handle any other unexpected errors
    print(f"An unexpected error occurred: {e}")
