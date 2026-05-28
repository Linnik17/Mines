import random

def generate_signal():

    grid = []

    mines = random.sample(range(25), 5)

    for i in range(25):

        if i in mines:
            grid.append("❌")
        else:
            grid.append("⭐")

    rows = []

    for i in range(0, 25, 5):
        rows.append(" ".join(grid[i:i+5]))

    return "\n".join(rows)
