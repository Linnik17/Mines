import json
import os
import random
import numpy as np

HISTORY_FILE = "history.json"

GRID_SIZE = 25
MINES_COUNT = 5


def load_history():

    if not os.path.exists(HISTORY_FILE):
        return []

    with open(HISTORY_FILE, "r") as f:
        return json.load(f)


def save_history(history):

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f)


def analyze_history(history):

    heatmap = np.zeros(GRID_SIZE)

    for game in history:
        for mine in game:
            heatmap[mine] += 1

    return heatmap


def generate_mines(heatmap):

    safest = np.argsort(heatmap)

    safe_zone = safest[:20]

    mines = random.sample(list(set(range(25)) - set(safe_zone[:15])), 5)

    return mines


def render_grid(mines):

    result = []

    for i in range(GRID_SIZE):

        if i in mines:
            result.append("❌")
        else:
            result.append("⭐")

    rows = []

    for i in range(0, GRID_SIZE, 5):
        rows.append(" ".join(result[i:i+5]))

    return "\n".join(rows)


def confidence(heatmap):

    avg = np.mean(heatmap)

    score = max(70, 95 - int(avg))

    return score


def generate_signal():

    history = load_history()

    heatmap = analyze_history(history)

    mines = generate_mines(heatmap)

    history.append(mines)

    if len(history) > 200:
        history.pop(0)

    save_history(history)

    grid = render_grid(mines)

    conf = confidence(heatmap)

    return grid, conf
