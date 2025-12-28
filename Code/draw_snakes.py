# draws snakes within the settings menu

import turtle

import settings_vals
from Code import create

built_snakes = [
    {
        "id": 0,
        "head": None,  # placeholder
        "segments": [],
        "controller": None,
    }
]

def build_tail(tail_col, start_x, start_y):
    tails = []
    for i in range(3):
        tail = turtle.Turtle()
        create.make_asset(tail, 0, "square", tail_col, start_x, start_y - (i+1)*20)
        tails.append(tail)
    return tails

def build_snake(_wn, var_name):
    if var_name not in ["p1h", "p1t", "p2h", "p2t"]:
        return

    player = var_name[:2]  # "p1" or "p2"
    player_num = int(player[1])  # 1 or 2
    head_var = player + "h"
    tail_var = player + "t"

    # Position based on player: p1 left, p2 right
    start_x = -40 if player_num == 1 else 40
    start_y = 40

    head_col = settings_vals.fetch_color(head_var)
    head = turtle.Turtle()
    create.make_asset(head, 0, "square", head_col, start_x, start_y)

    segments = []
    if var_name.endswith("t"):
        tail_col = settings_vals.fetch_color(tail_var)
        segments = build_tail(tail_col, start_x, start_y)

    # Add to built_snakes
    built_snakes.append({
        "id": len(built_snakes),
        "head": head,
        "segments": segments,
        "controller": None,
    })

def destroy_snakes(_wn):
    for snake in built_snakes:
        if snake["head"]:
            snake["head"].hideturtle()
        for seg in snake["segments"]:
            seg.hideturtle()
    built_snakes.clear()
    # Reset to initial state
    built_snakes.append({
        "id": 0,
        "head": None,
        "segments": [],
        "controller": None,
    })
    _wn.update()

def snakes_init(_wn):
    destroy_snakes(_wn)
    build_snake(_wn, "p1h")
    build_snake(_wn, "p1t")
    build_snake(_wn, "p2h")
    build_snake(_wn, "p2t")
    _wn.update()
    