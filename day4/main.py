
from collections import deque

with open("data.aoc", "r") as file:
    raw_data = [line.strip() for line in file.readlines()]
    file.close()

TOTAL_POINTS = 0 
card_ids = []
card_dict = {}

TOTAL_CARDS = 0

for line in raw_data:
    card, nums = line.split(": ")
    _, card_id = card.split()
    card_id = int(card_id)
    winning, obtained = nums.split(" | ")
    winning = [int(i) for i in winning.split()]
    obtained = [int(i) for i in obtained.split()]

    points = 0
    matches = 0

    for num in winning:
        if num in obtained:
            if points >= 1:
                points *= 2
            else:
                points += 1
            matches += 1
            
    
    card_dict[card_id] = matches
    card_ids.append(card_id)
    TOTAL_POINTS += points

queue = deque(card_ids)

while queue:
    card_id = queue.popleft()
    TOTAL_CARDS += 1

    for i in range(card_dict[card_id]):
        card_id += 1
        queue.append(card_id)


print("Part 1:", TOTAL_POINTS)
print("Part 2:", TOTAL_CARDS)

