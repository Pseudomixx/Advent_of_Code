import re

def get_value(cal_doc: str):

    lines = cal_doc.splitlines()
    sum_values = 0
    
    # positive lookahead assertion to find overlapping digit names:
    # e.g.: "twone" = "two" and "one"
    pattern = re.compile(r"(?=(one|two|three|four|five|six|seven|eight|nine|zero|\d))")
    # list of words to be converted into integers
    digits = ["zero", "one", "two", "three", "four", "five", "six", "seven",
              "eight", "nine"]
    
    for line in lines:
        matches = re.findall(pattern, line)
        first_digit = matches[0]
        last_digit = matches[-1]
        
        # Convert words into integers
        if first_digit in digits:
            first_digit = digits.index(first_digit)
        if last_digit in digits:
            last_digit = digits.index(last_digit)

        # Concatenate the digits
        line_value = str(first_digit) + str(last_digit)
        # Convert to integer and add to total value
        sum_values += int(line_value)

    return sum_values


file = open("day_1_data.txt")
input = file.read()

print(get_value(input))