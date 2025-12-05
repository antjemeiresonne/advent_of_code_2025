test_ranges = [[3,5], [10,14], [16,20], [12,18]]
test_ids = [1, 5, 8, 11, 17, 32]

puzzle_input = open('five.txt').read().strip().split('\n')
puzzle_ranges = puzzle_input[:puzzle_input.index('')]
nestedInput = [list(map(int, pair.split("-"))) for pair in puzzle_ranges]
puzzle_ids = puzzle_input[puzzle_input.index('')+1:]

def merge(intervals):
    intervals.sort(key=lambda x: x[0])

    merged_intervals = [intervals[0]]

    for current in intervals[1:]:
        last_merged = merged_intervals[-1]

        if current[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current[1])
        else:
            merged_intervals.append(current)

    return merged_intervals

def count_valid_ids(input):
    merged_intervals = merge(input)
    print(merged_intervals)
    count = 0
    for interval in merged_intervals:
        count += len(range(interval[0], interval[1]+1))
    return count


print(count_valid_ids(nestedInput))