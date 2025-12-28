# Carries out actions related to the binds in module key_binds.py

from Code import game_starter
from Code import game_engine
from Code import writing
from Code import settings
from Code import draw_snakes

in_settings = False

# (out of settings utility), (in settings utility)
# Start singleplayer, modify amount of food
def bind_1(_wn):
    if not in_settings:
        game_starter.start_mode_1(_wn)
    else:
        settings.cycle_apples()
        writing.write_settings()

# Start multiplayer, modify dimensions
def bind_2(_wn):
    if not in_settings:
        game_starter.start_mode_2(_wn)
    else:
        settings.cycle_dimensions(_wn)
        writing.write_settings()

# NULL, change speed-up boolean
def bind_3(_wn):
    if in_settings:
        settings.cycle_speedup()
        writing.write_settings()

# NULL, change player 1 head color
def bind_4(_wn):
    if in_settings:
        settings.cycle_color(_wn, "p1h")
        writing.write_settings()

# NULL, change player 1 tail color
def bind_5(_wn):
    if in_settings:
        settings.cycle_color(_wn, "p1t")
        writing.write_settings()

# NULL, change player 2 head color
def bind_6(_wn):
    if in_settings:
        settings.cycle_color(_wn, "p2h")
        writing.write_settings()

# NULL, change player 2 tail color
def bind_7(_wn):
    if in_settings:
        settings.cycle_color(_wn, "p2t")
        writing.write_settings()

# NULL, change background color
def bind_8(_wn):
    if in_settings:
        settings.cycle_color(_wn, "background")
        writing.write_settings()

# End current game, exit settings (if in settings)
def bind_space(_wn):
    global in_settings
    if in_settings:
        in_settings = False
        writing.write_menu()
        draw_snakes.destroy_snakes(_wn)
    elif game_engine.Playing:
        game_starter.end_game()
    else:
        in_settings = True
        writing.write_settings()
        # draw_snakes.snakes_init(_wn)