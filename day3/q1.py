import re

filename = 'input.txt'

results = None
to_sum = []
with open(filename) as file:
    for line in file:
        # Lets use regex to find a specific pattern
        results = re.findall(r'mul\(\d{1,3},\d{1,3}\)', line)
        for multiplier in results:
            # Lets just use regex to find the numbers too
            numbers = re.findall(r'\d{1,3}', multiplier)
            # This should always come to two numbers
            to_sum.append(int(numbers[0]) * int(numbers[1]))

print(sum(to_sum))

print(results)