# Mad Libs Generator

print("Welcome to the Mad Libs Generator!")
# Get words from the user
continent = input("enter a continent: ")
name = input("Enter a name: ")
adjective = input("Enter an adjective: ")
animal = input("Enter an animal: ")
verb = input("Enter a verb: ")
place = input("Enter a place: ")
food = input("Enter a food: ")

# Create the story using an f-string
story = f"""
One day in {continent}, {name} went to the {place}.
On the way, they saw a very {adjective} {animal}.
The {animal} started to {verb}!
{name} was surprised and decided to give it some {food}.
It was the strangest day ever!
"""

# Display the story
print("\n--- Your Mad Libs Story ---")
print(story)