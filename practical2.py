# Model-Based Intelligent Agent
# Grid Navigation with Obstacles

grid = [
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

# Internal state
current = start
visited = set()
path = [current]

# Possible movements
moves = [
    (-1, 0), # Up
    (1, 0), # Down
    (0, -1), # Left
    (0, 1) # Right
]

while current != goal:

    visited.add(current)
    found = False

    for move in moves:
        new_row = current[0] + move[0]
        new_col = current[1] + move[1]

        # Check valid position
        if (0 <= new_row < len(grid) and
            0 <= new_col < len(grid[0])):

            # Check obstacle and visited cell
            if (grid[new_row][new_col] == 0 and
                (new_row, new_col) not in visited):

                current = (new_row, new_col)
                path.append(current)
                found = True
                break

    if not found:
        print("No path found!")
        break

if current == goal:
    print("Goal reached!")
    print("Navigation Path:")

    for position in path:
        print(position)
