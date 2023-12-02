import re

# ---------------------------------------------------------------------------
# Solution 1:
def sum_possible_game_ids(input: str):
    games = input.splitlines()

    sum_ids = 0

    for game in games:
        if game_possible(game):
            sum_ids += get_game_id(game)
    
    return sum_ids


def game_possible(game: str):

    game_id, game_contents = game.split(": ")
    game_sets = [set for set in game_contents.split("; ")]
    max_cubes = {"red": 12, "green": 13, "blue": 14}

    for set in game_sets:
        set_dict = get_set_dict(set)
        for color, amount in set_dict.items():
            if amount > max_cubes[color]:
                return False
    return True


def get_game_id(game: str):

    game_id, game_contents = game.split(": ")
    index = game_id.split(" ")[1]
    return int(index)


def get_set_dict(set):

    pattern = re.compile(r"(?P<amount>\d+) (?P<color>\w+)")
    matches = re.findall(pattern, set)
    set_dict = {}
    for cube_count in matches:
        amount = int(cube_count[0])
        color = cube_count[1]
        set_dict[color] = amount

    return set_dict


# ---------------------------------------------------------------------------
# Solution 2:    
def get_minimum_set(game):
    game_id, game_contents = game.split(": ")
    game_sets = [set for set in game_contents.split("; ")]

    minimum_set = {"red": 0, "green": 0, "blue": 0}

    for set in game_sets:
        set_dict = get_set_dict(set)
        for color, amount in set_dict.items():
            if amount > minimum_set[color]:
                minimum_set[color] = amount
    
    return minimum_set

def get_set_power(set: dict):

    numbers = set.values()
    power = 1
    for i in numbers:
        power *= i
    return power

def get_sum_powers(input: str):

    games = input.splitlines()

    power_sum = 0

    for game in games:
        minimum_set = get_minimum_set(game)
        set_power = get_set_power(minimum_set)
        power_sum += set_power

    return power_sum


file = open("day_2_data.txt")
contents = file.read()

print("Sum of possible game IDs: ", sum_possible_game_ids(contents))

print("Sum of minimum set powers: ", get_sum_powers(contents))


