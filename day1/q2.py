filename = 'q1_input.txt'

list1 = []
list2 = []
similarity_score = 0
with open(filename) as f:
    for line in f:
        line = line.strip()
        line = line.split(' ')
        list1.append(int(line[0]))
        list2.append(int(line[-1]))

for x in list1:
    number_of = list2.count(x)
    similarity_score += x * number_of

print(similarity_score)