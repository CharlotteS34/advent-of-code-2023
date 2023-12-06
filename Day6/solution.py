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
    return input

def get_part_1_solution(input):
    times = [int(time) for time in input[0].replace('\n', '').split(" ") if time.isdigit()]
    distances = [int(distance) for distance in input[1].split(" ") if distance.isdigit()]
    total = 1
    for i in range(0, len(times)):
        total*=number_of_ways_to_beat_record(times[i], distances[i])
    return total

def get_part_2_solution(input):
    times = [time for time in input[0].replace('\n', '').split(" ") if time.isdigit()]
    distances = [distance for distance in input[1].split(" ") if distance.isdigit()]
    total_time = ""
    for time in times:
        total_time+=time
    total_distance = ""
    for distance in distances:
        total_distance+=distance
    return number_of_ways_to_beat_record(int(total_time), int(total_distance))

def number_of_ways_to_beat_record(time, distance_record):
    return len([button_time for button_time in range(0, time) if distance_record < distance_travelled(button_time, time)])

def distance_travelled(button_time, total_time):
    speed = button_time
    time = total_time - button_time
    return speed * time

print("testing part 1 solution")
test_input = get_test_input()
print(get_part_1_solution(test_input))
print("Part 1 solution")
input = get_puzzle_input()
print(get_part_1_solution(input))

print("testing part 2 solution")
test_input = get_test_input()
print(get_part_2_solution(test_input))
print("Part 2 solution")
input = get_puzzle_input()
print(get_part_2_solution(input))