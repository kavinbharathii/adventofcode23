
with open("data.aoc", "r") as file:
    raw_data = [line.strip() for line in file.readlines()]
    file.close()

TOTAL_RED = 12
TOTAL_GREEN = 13
TOTAL_BLUE = 14

TOTAL_GAME_ID = 0
TOTAL_POWER = 0

for line in raw_data:
    game_index, game_data = line.split(': ')
    games = game_data.split('; ')

    game_red_set = []
    game_green_set = []
    game_blue_set = []
    game_possibility = True

    # for each individual game in a game set
    for game in games:
        game_red = 0
        game_green = 0
        game_blue = 0

        game = game.split(', ')
        for value in game:
                cubes, color = value.split()
                if "red" in value:
                    game_red += int(cubes)
                if "green" in value:
                    game_green += int(cubes)
                if "blue" in value:
                    game_blue += int(cubes)

        game_red_set.append(game_red)
        game_green_set.append(game_green)
        game_blue_set.append(game_blue)

        # if the possibility rule fails, count out the game as impossible
        if game_red > TOTAL_RED or game_green > TOTAL_GREEN or game_blue > TOTAL_BLUE:
            game_possibility = False

    game_cube_set = [max(game_red_set), max(game_green_set), max(game_blue_set)]
    game_power = 1
    for i in game_cube_set:
        game_power *= i

    TOTAL_POWER += game_power

    # if the game still holds possible, then add it to the TOTAL_GAME_ID
    if game_possibility:
        game_id = int(game_index.strip(':').split()[-1])
        TOTAL_GAME_ID += game_id

print("Part 1:", TOTAL_GAME_ID)
print("Part 2:", TOTAL_POWER)
