#!/usr/bin/env python3

# Import the 'random' module to enable random selection from a list.
import random
import os # Import the 'os' module to handle file paths.

# Define the name of the file containing affirmations.
AFFIRMATIONS_FILE = "affirmations.txt"

# Initialize an empty list to store affirmations read from the file.
affirmations = []

# --- Changes start here ---

try:
    # Get the directory of the current script.
    # This helps in locating the affirmations.txt file if the script is run from a different directory.
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, AFFIRMATIONS_FILE)

    # Open the affirmations file in read mode ('r').
    # 'with' statement ensures the file is properly closed after its block finishes.
    with open(file_path, 'r') as file:
        # Read each line from the file, strip leading/trailing whitespace (like newlines),
        # and add it to the 'affirmations' list.
        for line in file:
            stripped_line = line.strip()
            if stripped_line: # Only add non-empty lines
                affirmations.append(stripped_line)

except FileNotFoundError:
    # Handle the case where the affirmations file does not exist.
    print(f"Error: The file '{AFFIRMATIONS_FILE}' was not found in the same directory as the script.")
    print("Please make sure 'affirmations.txt' exists and contains your affirmations.")
    # Exit or handle gracefully if the file is essential. For this script, we'll just print an error.
    exit(1) # Exit the script if the file is not found.
except Exception as e:
    # Catch any other potential errors during file reading.
    print(f"An error occurred while reading the affirmations file: {e}")
    exit(1)

# Check if any affirmations were loaded.
if not affirmations:
    print(f"Warning: No affirmations were loaded from '{AFFIRMATIONS_FILE}'. The file might be empty.")
    exit(1)

# --- Changes end here ---

# Randomly select one affirmation from the list.
# The 'random.choice()' function picks a random element from the given sequence.
selected_affirmation = random.choice(affirmations)

# Print the selected affirmation to the console.
print("Your affirmation for today:")
print(selected_affirmation)
