#!/usr/bin/env python3

# Import the 'random' module to enable random selection from a list.
import random

# Define a list of positive affirmations.
# You can add as many affirmations as you like to this list.
affirmations = [
    "I am capable of achieving my goals.",
    "Every day is a new opportunity for growth.",
    "I am worthy of love and happiness.",
    "I embrace challenges as opportunities to learn and evolve.",
    "I am grateful for all the good in my life.",
    "I radiate positivity and attract abundance.",
    "I trust my intuition and make wise decisions."
]

# Randomly select one affirmation from the list.
# The 'random.choice()' function picks a random element from the given sequence.
selected_affirmation = random.choice(affirmations)

# Print the selected affirmation to the console.
print("Your affirmation for today:")
print(selected_affirmation)

