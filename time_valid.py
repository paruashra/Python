# Don't forget to import re!
import re


# Define is_valid_time below:
def is_valid_time(input_str):
    pattern = re.compile("^\d\d:\d{2}$")
    match = pattern.search(input_str)
    print(match)
    return True if match else False


print(is_valid_time("10:45"))
