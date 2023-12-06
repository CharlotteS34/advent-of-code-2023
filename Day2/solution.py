import os

def get_puzzle_input():
    file_name = (os.path.dirname(os.path.realpath(__file__)) + r"\input.txt")
    return read_input(file_name)

def get_test_input():
    file_name = (os.path.dirname(os.path.realpath(__file__)) + r"\test_input.txt")
    return read_input(file_name)

def read_input(file_name):
    input_file = open(file_name, 'r')
    input = input_file.readlines()
    input_file.close()
    return [s.replace('\n', '') for s in input]

def puzzle_solution_1(input):
    game_dict = convert_to_game_dict(input)
    valid_game_ids = [id for id in game_dict.keys() if all([game_set_is_below_limit(game_set) for game_set in game_dict[id]])]
    return sum(valid_game_ids)

def puzzle_solution_2(input):
    game_dict = convert_to_game_dict(input)
    powers = [get_power_of_game(game) for game in game_dict.values()]
    return sum(powers)

def get_power_of_game(game_set):
    min_red_value = max([val['red'] for val in game_set if 'red' in val.keys()])
    min_blue_value = max([val['blue'] for val in game_set if 'blue' in val.keys()])
    min_green_value = max([val['green'] for val in game_set if 'green' in val.keys()])
    return min_red_value * min_blue_value * min_green_value

def game_set_is_below_limit(game_set):
    limits_dict = {'red': 12, 'green': 13, 'blue': 14}
    colours = limits_dict.keys()
    return all([colour not in game_set.keys() or game_set[colour] <= limits_dict[colour] for colour in colours])

def convert_to_game_dict(input):
    game_dict = {}
    for line in input:
        game_label_and_value = line.replace(" ", "").split(":")
        game_id = int(game_label_and_value[0][4:])
        game_sets = [convert_game_set_to_dict(set) for set in game_label_and_value[1].split(';')]
        game_dict[game_id] = game_sets
    return game_dict

def convert_game_set_to_dict(game_set):
    dict = {}
    for game_set_item in game_set.split(','):
        val = get_val_from_game_set_item(game_set_item)
        dict[game_set_item[len(val):]] = int(val)
    return dict

def get_val_from_game_set_item(game_set_item):
    vals = [val for val in game_set_item if val.isdigit()]
    return ''.join(vals)

def game_set_is_below_limit_test():
    passed = True
    game_set_1 = {'red': 10, 'green': 13, 'blue': 13}
    if not game_set_is_below_limit(game_set_1):
        passed = False
        print ('game set 1 failed')
    game_set_2 = {'red': 13, 'green': 12, 'blue': 13}
    if game_set_is_below_limit(game_set_2):
        passed = False
        print ('game set 2 failed')
    game_set_3 = {'red': 10, 'green': 14, 'blue': 13}
    if game_set_is_below_limit(game_set_3):
        passed = False
        print ('game set 3 failed')
    game_set_4 = {'red': 10, 'green': 12, 'blue': 15}
    if game_set_is_below_limit(game_set_4):
        passed = False
        print ('game set 4 failed')
    if (passed):
        print('All game_set_is_below_limit_test tests passed')

def puzzle_solution_1_test():
    input = get_test_input()
    solution = puzzle_solution_1(input)
    if (solution == 8):
        print("Puzzle 1 test passed")
    else:
        print("Puzzle 1 test failed")

def puzzle_solution_2_test():
    input = get_test_input()
    solution = puzzle_solution_2(input)
    if (solution == 2286):
        print("Puzzle 2 test passed")
    else:
        print("Puzzle 2 test failed")

puzzle_solution_1_test()
print("Puzzle 1 solution: " + str(puzzle_solution_1(get_puzzle_input())))
puzzle_solution_2_test()
print("Puzzle 2 solution: " + str(puzzle_solution_2(get_puzzle_input())))