def destroy_game(wn, players, foods):
    # destroy foods
    for food in foods:
        food.hideturtle()
        food.clear()
        food.goto(10000, 10000)
    foods.clear()

    for player in players:
        # destroy head
        head = player["head"]
        head.hideturtle()
        head.clear()
        head.goto(10000, 10000)

        # destroy segments
        for seg in player["segments"]:
            seg.hideturtle()
            seg.clear()
            seg.goto(10000, 10000)

        player["segments"].clear()

    wn.update()
