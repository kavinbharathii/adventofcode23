

# Advent Of Code: day6

with open("data.aoc", "r") as file:
    raw_data = [line.strip() for line in file.readlines()]
    file.close()

_, *_times = raw_data[0].split()
times = [int(i) for i in _times]

_, *_dists = raw_data[1].split()
dists = [int(i) for i in _dists]

# part 1

result = 1

for index, time in enumerate(times):
    ways_to_win = 0

    for millisecond in range(time):
        distance_covered = millisecond * (time - millisecond)
        
        if distance_covered > dists[index]:
            ways_to_win += 1

    if ways_to_win > 0:
        result *= ways_to_win

print(f"Part 1: {result}")

# part 2

total_time = int(''.join(str(i) for i in times))
total_dist = int(''.join(str(i) for i in dists))

for millisecond in range(total_time):
    distance_covered = millisecond * (total_time - millisecond)

    if distance_covered > total_dist:
        break

ways_to_win = len(range(millisecond, total_time - millisecond + 1))
print(f"Part 2: {ways_to_win}")
