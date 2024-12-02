from typing import List


filename = 'input.txt'

no_of_safe = 0
no_of_unsafe = 0

def check_report_safety(line: List[int]) -> bool:
    # Get the diffs for the whole line
    diffs = [line[x]-line[x+1] for x in range(len(line)-1)]
    return (
        all([1 <= d <= 3 for d in diffs])
        or all ([-3 <= d <= -1 for d in diffs])
    )

with open(filename) as f:
    for line in f:
        line = line.split(' ')
        line = [int(x) for x in line]
        
        if check_report_safety(line) == True:
            no_of_safe += 1
        else:
            if any(check_report_safety(line[:i] + line[i+1:]) 
                for i in range(len(line))):
                no_of_safe += 1
            else:
                no_of_unsafe += 1
                
    print(no_of_safe, no_of_unsafe)