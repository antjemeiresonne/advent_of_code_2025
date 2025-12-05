test_input = [987654321111111, 811111111111119, 234234234234278, 818181911112111]
puzzle_input = open('three.txt').read().strip().split('\n')

def calculate_total_joltage(banks: list, amount_of_batteries: int):
    total_joltage = 0

    for bank in banks:
        digits = [int(d) for d in str(bank)]
        last_pos = 0
        result_digits = []

        for _ in range(amount_of_batteries):
            if last_pos >= len(digits):
                break
            remaining = amount_of_batteries - len(result_digits)
            search_space = digits[last_pos:len(digits) - remaining + 1]

            max_digit = max(search_space)
            max_index = search_space.index(max_digit) + last_pos

            result_digits.append(str(max_digit))
            last_pos = max_index + 1

        total_joltage += int("".join(result_digits))

    return total_joltage



print(calculate_total_joltage(puzzle_input, 12))