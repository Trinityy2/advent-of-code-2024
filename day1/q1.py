filename = 'q1_input.txt'


list1 = []
list2 = []
distance = []
with open(filename) as f:
    for line in f:
        line = line.strip()
        line = line.split(' ')
        list1.append(int(line[0]))
        list2.append(int(line[-1]))


list1.sort()
list2.sort()

for x in range(len(list1)):
    distance.append(abs(list1[x] - list2[x]))

print(sum(distance))