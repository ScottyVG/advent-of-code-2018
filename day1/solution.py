import itertools

#Part1
data = [int(x) for x in open("input.txt").readlines()]
print(sum(data))

#Part2
frequency = 0
accumulator = {0}
for count in itertools.cycle(data):
    frequency += count
    if frequency in accumulator:
        print(frequency); break
    accumulator.add(frequency)
