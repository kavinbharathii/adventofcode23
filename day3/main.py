
with open("data.aoc", "r") as file:
    raw_data = [line.strip() for line in file.readlines()]
    file.close()


# ------------------------------------------- functions ------------------------------------------- #

def adjacent_points(point_a, point_b):
    ax, ay = point_a
    bx, by = point_b

    if abs(ax - bx) > 1 or abs(ay - by) > 1:
        return False
    
    return True

# ------------------------------------------------------------------------------------------------- #

syms = []
nums = []

r = 0
c = 0

for line in raw_data:
    num = ''
    num_indices = []
    for char in line:
        if char == '.':
            if not num == '':
                nums.append([int(num), num_indices])
                num = ''
                num_indices = []

        elif char.isdigit():
            num += char
            num_indices.append((r, c))

        else:
            if not num == '':
                nums.append([int(num), num_indices])
                num = ''
                num_indices = []

            syms.append((char, (r, c)))

        c += 1

    if not num == '':
        nums.append([int(num), num_indices])
        num = ''
        num_indices = []    

    r += 1
    c = 0

part_numbers = []
part_number_indices = []
gear_wheels = {}


for num, num_indices in nums:
    is_part_number = False

    for sym, sym_index in syms:
        for num_index in num_indices:
            if adjacent_points(num_index, sym_index):
                if sym == "*":
                    if sym_index not in gear_wheels.keys():
                        gear_wheels[sym_index] = [num]
                    else:
                        gear_wheels[sym_index].append(num)

                is_part_number = True
                break

    if is_part_number: 
        part_numbers.append(num)
        part_number_indices.extend(num_indices)

# Part 2: Gear ratios
gear_ratios = []

for index, nums in gear_wheels.items():
    if len(nums) == 2:
        gear_ratio = 1
        for num in nums:
            gear_ratio *= num

        gear_ratios.append(gear_ratio)


print("Part 1:", sum(part_numbers))
print("Part 2:", sum(gear_ratios))
