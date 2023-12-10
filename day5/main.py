

# Advent Of Code: day5

with open("data.aoc", "r") as file:
    raw_data = [line.strip() for line in file.readlines()]
    file.close()

seed_to_soil_map = []
soil_to_fertilizer_map = []
fertilizer_to_water_map = []
water_to_light_map = []
light_to_temp_map = []
temp_to_humidity_map = []
humidity_to_location_map = []
seed_to_location_mapping = [seed_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map, water_to_light_map, light_to_temp_map, temp_to_humidity_map, humidity_to_location_map]

for line in raw_data:
    
    if "seeds" in line:
        _, seeds_nums = line.split(": ")
        seeds = [int(i) for i in seeds_nums.split()]

    elif "seed-to-soil" in line:
        current_map = seed_to_soil_map

    elif "soil-to-fertilizer" in line:
        current_map = soil_to_fertilizer_map

    elif "fertilizer-to-water" in line:
        current_map = fertilizer_to_water_map

    elif "water-to-light" in line:
        current_map = water_to_light_map

    elif "light-to-temperature" in line:
        current_map = light_to_temp_map

    elif "temperature-to-humidity" in line:
        current_map = temp_to_humidity_map

    elif "humidity-to-location" in line:
        current_map = humidity_to_location_map

    elif line == "":
        current_map = None

    else:
        _destination, _source, _range = [int(i) for i in line.split()]
        current_map.append((_destination, _source, _range))


def get_closest_seed_location(seeds):
    seed_locations = []

    for seed in seeds:
        for mapping in seed_to_location_mapping:

            for dest, source, rang in mapping:
                if (seed >= source) and (seed < source + rang):
                    seed = dest + (seed - source)
                    break

        seed_locations.append(seed)

    return min(seed_locations)

print(get_closest_seed_location(seeds))


seed_ranges = []

for i in range(0, len(seeds), 2):
    seed_ranges.append((seeds[i], seeds[i] + seeds[i + 1]))

for mapping in seed_to_location_mapping:

    new = []

    while len(seed_ranges) > 0:
        start, end = seed_ranges.pop()
        
        for _destination, _start, _range in mapping:
            overlap_start = max(start, _start)
            overlap_end = min(end, _start + _range)

            if overlap_start < overlap_end:
                new.append((overlap_start - _start + _destination, overlap_end - _start + _destination))

                if overlap_start > start:
                    seed_ranges.append((start, overlap_start))

                if end > overlap_end:
                    seed_ranges.append((overlap_end, end))

                break

        else:
            new.append((start, end))

    seed_ranges = new

print(min(seed_ranges)[0])
