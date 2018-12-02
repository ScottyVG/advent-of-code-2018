import itertools

from collections import Counter

#Part1
data = open("input.txt", "r")
split_data = data.read().strip().split()
data.close()

# print(split_data)

counts = [0, 0]
for i in split_data:
	iterator = [j for i,j in Counter(i).most_common()]
	if 3 in iterator:
		counts[0] += 1
	if 2 in iterator:
		counts[1] += 1

checksum = counts[0] * counts[1]
print(checksum)

#Part2
for i in split_data:
	for j in split_data:
		differences = 0
		for index, check in enumerate(i):
			if check != j[index]:
				differences += 1
		if differences == 1:
			result = [check for index, check in enumerate(i) if j[index] == check]
			print(''.join(result))