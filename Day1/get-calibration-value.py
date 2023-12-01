def find_first_digit_match(text, digits):
    digits_list = digits.keys()
    for i, char in enumerate(text):
        if (char.isdigit()):
            return str(char)
        text_to_check = text[0:i+1]
        digit_matches = [d for d in digits_list if d in text_to_check]
        if (len(digit_matches) > 0):
            digit_match = digit_matches[0]
            return digits[digit_match]
    return ""

def get_second_calibration_value(text):
    print(text)
    digits = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    first_digit = find_first_digit_match(text, digits)
    digits_backwards = {"eno": "1", "owt": "2", "eerht": "3", "ruof": "4", "evif": "5", "xis": "6", "neves": "7", "thgie": "8", "enin": "9"}
    last_digit = find_first_digit_match(text[::-1], digits_backwards)
    return int(first_digit + last_digit)

def get_calibration_value(text):
    text_list = [char for i,char in enumerate(text)]
    digits = [d for d in text_list if d.isdigit()]
    return int(digits[0] + digits[-1])

def get_total_calibration_value(text_list):
    calibration_values = [get_calibration_value(t) for t in text_list]
    return sum(calibration_values)

def get_second_total_calibration_value(text_list):
    calibration_values = [get_second_calibration_value(t) for t in text_list]
    return sum(calibration_values)

def read_input(file_name):
    input_file = open(file_name, 'r')
    input = input_file.readlines()
    input_file.close()
    return input

def puzzle_solution_1(file_name):
    input = read_input(file_name)
    return get_total_calibration_value(input)

def puzzle_solution_2(file_name):
    input = read_input(file_name)
    return get_second_total_calibration_value(input)

print("Testing")
print("1abc2: " + str(get_calibration_value("1abc2")))
print("pqr3stu8vwx: " + str(get_calibration_value("pqr3stu8vwx")))
print("a1b2c3d4e5f: " + str(get_calibration_value("a1b2c3d4e5f")))
print("treb7uchet: " + str(get_calibration_value("treb7uchet")))
test_input = "1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet".splitlines()
print("Test total: " + str(get_total_calibration_value(test_input)))

file_name = "C:\\Code\\Fun\\advent-of-code-2023\\Day1\\input.txt"
print("Solution value: " + str(puzzle_solution_1(file_name)))

print("Testing 2")
test_text = "two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen"
test_text_list = test_text.splitlines()
print(get_second_calibration_value("zoneight234"))
print("RESULT " + str(get_second_total_calibration_value(test_text_list)))
print("Solution value: " + str(puzzle_solution_2(file_name)))