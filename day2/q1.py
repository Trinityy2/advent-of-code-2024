filename = 'input.txt'

no_of_safe = 0
no_of_unsafe = 0

with open(filename) as f:
    for line in f:
        line = line.split(' ')
        line = [int(x) for x in line]
        
        order = ''
        if line == sorted(line):
            # Line is ascending
            order = 'ASC'
        elif line == sorted(line, reverse=True):
            order = 'DESC'
        else:
            print("not_sorted", line)
            no_of_unsafe += 1
            continue

        safe = True
        for x in range(1,len(line)):
            diff = line[x-1] - line[x]
            if not (abs(diff) > 0 and abs(diff) <= 3):
                safe = False
                break

        if safe:
            print("Safe", line)
            no_of_safe += 1
        else: 
            print("Unsafe", line)
            no_of_unsafe += 1

    print(no_of_safe, no_of_unsafe)