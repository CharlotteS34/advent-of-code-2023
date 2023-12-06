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

class Map:
    def __init__(self, map_name):
        self.map_name = map_name
        self.map_lines = []

    def add_map_line(self, map_line_input):
        self.map_lines.append(MapLine(int(map_line_input.split(" ")[0], ), int(map_line_input.split(" ")[1], ), int(map_line_input.split(" ")[2], )))

    def map_source_to_destination(self, source_number):
        matching_map_lines = [map_line for map_line in self.map_lines if source_number in range(map_line.source_range_start, map_line.source_range_start + map_line.range_length)]
        if (len(matching_map_lines) == 0):
            return source_number
        else:
            map_line = matching_map_lines[0]
            return map_line.destination_range_start + source_number - map_line.source_range_start        

class MapLine:
    def __init__(self, destination_range_start, source_range_start, range_length):
        self.destination_range_start = destination_range_start
        self.source_range_start = source_range_start
        self.range_length = range_length

def match_source_to_destination_test():
    map = Map("seed-to-soil map:")
    map.add_map_line("50 98 2")
    map.add_map_line("52 50 48")
    val = map.map_source_to_destination(53)
    if (val == 55):
        print("PASSED: match_source_to_destination_test")
    else:
        print("FAILED: match_source_to_destination_test")

class IslandAlmanac:
    def __init__(self, input):
        self.seeds = [int(seed) for seed in input[0].split(":")[1].split(" ")[1:]]
        self.maps = {}
        current_map = None
        for line in input[2:]:
            if (current_map == None):
                current_map = Map(line.replace('\n', '').replace(':', ''))
                continue
            if (line == '\n' or line == input[-1]):
                self.maps[current_map.map_name] = current_map
                current_map = None
                continue
            current_map.add_map_line(line)

    def get_location_number_from_seed(self, seed_number):
        soil_number = self.maps["seed-to-soil map"].map_source_to_destination(seed_number)
        fertilizer_number = self.maps["soil-to-fertilizer map"].map_source_to_destination(soil_number)
        water_number = self.maps["fertilizer-to-water map"].map_source_to_destination(fertilizer_number)
        light_number = self.maps["water-to-light map"].map_source_to_destination(water_number)
        temperature_number = self.maps["light-to-temperature map"].map_source_to_destination(light_number)
        humidity_number = self.maps["temperature-to-humidity map"].map_source_to_destination(temperature_number)
        location_number = self.maps["humidity-to-location map"].map_source_to_destination(humidity_number)
        print(len(self.maps["humidity-to-location map"].map_lines))
        return location_number
    
    def get_minimum_location_number(self):
        location_numbers = [self.get_location_number_from_seed(seed_number) for seed_number in self.seeds]
        return min(location_numbers)

        
match_source_to_destination_test()
print("testing part 1 solution")
test_input = get_test_input()
almanac = IslandAlmanac(test_input)
print(almanac.get_minimum_location_number())
# print("Part 1 solution")
# input = get_puzzle_input()
# almanac = IslandAlmanac(input)
# print(almanac.get_minimum_location_number())
