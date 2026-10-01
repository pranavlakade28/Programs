# Simple Vacuum Cleaner Program

# Environment
rooms = {
    "A": "Dirty",
    "B": "Clean"
}

# Vacuum starts in Room A
location = "A"

for i in range(2):
    print("Vacuum is in Room", location)

    if rooms[location] == "Dirty":
        print("Room is Dirty. Cleaning...")
        rooms[location] = "Clean"
    else:
        print("Room is already Clean.")

    # Move to the other room
    if location == "A":
        location = "B"
    else:
        location = "A"

print("\nFinal Room Status:")
print(rooms)