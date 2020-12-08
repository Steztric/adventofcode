import re

def get_puzzle(day):
    with open(f"day{day}.txt") as f:
        return [line.replace("\n", "") for line in f.readlines()]

def get_puzzle_raw(day):
    with open(f"day{day}.txt") as f:
        return f.read()

def convert_to_integers(input):
    return [int(l) for l in input]

def solve_puzzle_1a(input):
    for i in range(len(input) - 1):
        for j in range(i, len(input) - 1):
            if input[i] + input[j] == 2020:
                return input[i] * input[j]

def solve_puzzle_1b(input):
    target = 2020
    pairs_sums = {};
    for i in range(len(input) - 1):
        for j in range(i + 1, len(input) - 1):
            pair_sum = input[i] + input[j]
            if pair_sum <= target:
                pairs_sums[(i, j)] = pair_sum

    for k in range(2, len(input) - 1):
        for key, pair_sum in pairs_sums.items():
            if pair_sum + input[k] == target:
                i, j = key
                return input[i] * input[j] * input[k]

def tokenise_password_rules(input):
    tokens = [re.split("-| |: ", line) for line in input]
    return [(int(t[0]), int(t[1]), t[2], t[3]) for t in tokens]

def solve_puzzle_2a(input):
    valid = 0
    for password in input:
        count = 0
        for letter in password[3]:
            if letter == password[2]:
                count += 1
        if count >= password[0] and count <= password[1]:
            valid += 1

    return valid

def solve_puzzle_2b(input):
    valid = 0
    for entry in input:
        first_pos, second_pos, letter, password = entry
        occurrances = 0
        if password[first_pos-1] == letter:
            occurrances += 1
        if password[second_pos-1] == letter:
            occurrances += 1
        if occurrances == 1:
            valid += 1
    
    return valid

def tokenise_tree_pattern(input):
    return [list(line) for line in input]

def tree_encounters(tokens, r_step, d_step):
    trees = lat = lon = 0
    height = len(tokens)
    width = len(tokens[0])
    while lon < height:
        if tokens[lon][lat] == '#':
            trees += 1
        lat += r_step
        lon += d_step
        if lat >= (width - 1):
            lat -= (width - 1)
            
    return trees

def solve_puzzle_3a(input):
    tokens = tokenise_tree_pattern(input)
    return tree_encounters(tokens, 3, 1)

def solve_puzzle_3b(input):
    tokens = tokenise_tree_pattern(input)
    r1d1 = tree_encounters(tokens, 1, 1)
    r3d1 = tree_encounters(tokens, 3, 1)
    r5d1 = tree_encounters(tokens, 5, 1)
    r7d1 = tree_encounters(tokens, 7, 1)
    r1d2 = tree_encounters(tokens, 1, 2)
    return r1d1 * r3d1 * r5d1 * r7d1 * r1d2

def tokenise_passport_deets(input):
    passports = input.split("\n\n")
    return [passport.replace("\n", " ") for passport in passports]

def solve_puzzle_4a(input):
    passports = tokenise_passport_deets(input)
    valid = 0
    for passport in passports:
        try:
            byr = re.search('byr\:([0-9]{4})', passport)
            if not byr:
                continue
            byr_num = int(byr[1])
            if byr_num < 1920 or byr_num > 2002:
                continue
            
            iyr = re.search('iyr\:([0-9]{4})', passport)
            if not iyr:
                continue
            iyr_num = int(iyr[1])
            if iyr_num < 2010 or iyr_num > 2020:
                continue
            
            eyr = re.search('eyr\:([0-9]{4})', passport)
            if not eyr:
                continue
            eyr_num = int(eyr[1])
            if eyr_num < 2020 or eyr_num > 2030:
                continue
            
            hgt = re.search('hgt\:([0-9]{2,3})(cm|in)', passport)
            if not hgt:
                continue
            hgt_num = int(hgt[1])
            if hgt[2] == "cm":
                if hgt_num < 150 or hgt_num > 193:
                    continue
            elif hgt[2] == "in":
                if hgt_num < 59 or hgt_num > 76:
                    continue
            
            hcl = re.search('hcl\:#[0-9a-f]{6}', passport)
            if not hcl:
                continue

            ecl = re.search('ecl\:(amb|blu|brn|gry|grn|hzl|oth)', passport)
            if not ecl:
                continue

            pid = re.search('pid\:[0-9]{9}', passport)
            if not pid:
                continue

            valid += 1

        except:
            continue
    
    return valid

def partitions_to_binary_array(partitions, identifier):
    return [1 if char == identifier else 0 for char in list(partitions)]

def binary_array_to_int(binary):
    return int(''.join(map(str, binary)), 2)

def seat_row_col(seat_map):
    row_binary = partitions_to_binary_array(seat_map[:7], "B")
    row = binary_array_to_int(row_binary)
    col_binary = partitions_to_binary_array(seat_map[-3:], "R")
    col = binary_array_to_int(col_binary)
    return (row, col)

def seat_id(row, col):
    return row * 8 + col

def solve_puzzle_5a(input):
    max = 0
    for seat_map in input:
        row, col = seat_row_col(seat_map)
        id = seat_id(row, col)
        if id > max:
            max = id

    return max

def solve_puzzle_5b(input):
    all_seats = [[False for _ in range(8)] for _ in range(128)]
    
    for seat_map in input:
        row, col = seat_row_col(seat_map)
        all_seats[row][col] = True
    
    return all_seats

def solve_puzzle_6a(input):
    groups = [group.replace("\n", "") for group in input.split("\n\n")]
    counts = [len(set(list(group))) for group in groups]
    return sum(counts)

def all_yes_count(group):
    group_size = len(group)
    counts = {}
    for i in range(ord('a'), ord('z') + 1):
        counts[chr(i)] = 0
    for person in group:
        for yes_char in list(person):
            counts[yes_char] += 1

    all_yes = 0
    for v in counts.values():
        if v == group_size:
            all_yes += 1

    return all_yes

def solve_puzzle_6b(input):
    groups = [group.split("\n") for group in input.split("\n\n")]
    counts = [all_yes_count(group) for group in groups]
    return sum(counts)

if __name__ == "__main__":
    input = get_puzzle_raw(6);
    sample = """abc

a
b
c

ab
ac

a
a
a
a

b"""
    answer = solve_puzzle_6b(input)
    print(answer)