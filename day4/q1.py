import re

filename = 'input.txt'

grid = []
with open(filename) as file:
    for line in file:
        grid.append(line.strip())

# Now we have to just do a greedy search in all possible lines
count = 0
pattern = r'X.*?M.*?A.*?S'
# Horizontal search
for line in grid:
    count += len(re.findall(pattern, line))
    count += len(re.findall(pattern, line[::-1]))

# Vertical search
for i in range(len(grid[0])):
    count += len(re.findall(pattern, ''.join([line[i] for line in grid])))
    count += len(re.findall(pattern,
                 ''.join([line[i] for line in grid[::-1]])))

# Diagonal search -- Something wrong here
for i in range(len(grid)):
    count += len(re.findall(pattern,
                 ''.join([grid[i+j][j] for j in range(len(grid)-i)])))
    count += len(re.findall(pattern,
                 ''.join([grid[j][i+j] for j in range(len(grid)-i)])))
    count += len(re.findall(pattern,
                 ''.join([grid[i+j][len(grid)-j-1] for j in range(len(grid)-i)])))
    count += len(re.findall(pattern,
                 ''.join([grid[j][len(grid)-i-j-1] for j in range(len(grid)-i)])))

print(count)
