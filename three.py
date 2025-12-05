test_input = [987654321111111, 811111111111119, 234234234234278, 818181911112111]
puzzle_input = open('three.txt').read().strip().split('\n')


def calculate_joltage(bank):
    bank_list = [int(x) for x in str(bank)]
    first_battery_position = str(bank).find(str(max(bank_list)))
    if first_battery_position == len(str(bank)) - 1:
        second_battery_position = str(bank).find(str(max(bank_list[:-1])))
        return int(str(bank_list[second_battery_position]) + str( bank_list[first_battery_position]))
    else:
        second_battery_position = str(bank).find(str(max(bank_list[first_battery_position + 1:])))
        return int(str(bank_list[first_battery_position]) + str( bank_list[second_battery_position]))

def calculate_total_joltage(banks):
    total_joltage = 0
    for bank in banks:
        joltage = calculate_joltage(int(bank))
        total_joltage += joltage
        print(f'Bank {bank} has joltage {joltage}')
    return total_joltage

print(calculate_total_joltage(puzzle_input))