import re

filename = 'input.txt'

results = None
to_sum = []
enabled = True

with open(filename) as file:
    for line in file:
        # Lets use regex to find a specific pattern
        results = [(m.start(), m.end())
                   for m in re.finditer(r'mul\(\d{1,3},\d{1,3}\)', line)]
        do_and_dont = [(m.start(), m.end())
                       for m in re.finditer(r'do\(\)|don\'t\(\)', line)]

        completed = False
        while not completed:
            # check to see if we have to consider changing enabled
            if len(do_and_dont) > 0 and do_and_dont[0][0] < results[0][0]:
                flag_changer = do_and_dont[0]
                test = line[flag_changer[0]:flag_changer[1]]
                enabled = False if 'don\'t()' in test else True
                do_and_dont.pop(0)
                continue

            # Add to sum if enabled
            multiplier = results.pop(0)
            if enabled:
                # Lets just use regex to find the numbers too
                numbers = re.findall(
                    r'\d{1,3}', line[multiplier[0]:multiplier[1]])
                # This should always come to two numbers
                to_sum.append(int(numbers[0]) * int(numbers[1]))

            if len(results) <= 0:
                completed = True

print(sum(to_sum))
