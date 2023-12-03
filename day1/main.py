
with open("data.aoc", "r") as file:
    raw_data = [line.strip() for line in file.readlines()]
    file.close()

total = 0

def replace_all_num(str):
    nums = {"one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"}
    
    for index, letter in enumerate(str):
        for num, value in nums.items():
            if str[index:].startswith(num):
                str = str[:index] + value + str[index + 1:]

    print(str)
    return str

for line in raw_data:
    line = replace_all_num(line)
    nums = [i for i in line if i.isdigit()]
    first = nums[0]
    last = nums[-1]
    print(first, last)
    num = int(first + last)
    total += num

print(total)


