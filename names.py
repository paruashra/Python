import re


def parse_name(input_str):
	name_regex = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$')
	matches = name_regex.search(input_str)
	print(matches.group())
	print(matches.group('first'))
	print(matches.group('last'))
	print(matches.group(2))
	print(matches.group(3))


parse_name("Mrs. Tilda Swinton")
