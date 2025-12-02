puzzle_input = open('one.txt').read().strip().split('\n')

print(puzzle_input)

def rotate_dial(dialposition, rotation):
    rotation_direction = rotation[0]
    rotation_amount = int(rotation[1:])
    times_pointed_at_zero =0
    if rotation_direction == 'R':
        times_pointed_at_zero = (dialposition + rotation_amount) // 100
        dialposition = dialposition + (rotation_amount % 100)
        if dialposition >= 100:
            dialposition = dialposition - 100

    if rotation_direction == 'L':
        if  dialposition == 0:
            dialposition = 100
        times_pointed_at_zero = - ((dialposition - 100) - rotation_amount) // 100
        dialposition = dialposition - (rotation_amount % 100)
        if dialposition < 0:
            dialposition = dialposition + 100

    return dialposition, times_pointed_at_zero

def calculate_password(steps, startposition):
    password = 0
    dial_position = startposition
    for step in steps:
        dial_position, times_pointed_at_zero = rotate_dial(dial_position, step)
        if times_pointed_at_zero > 0:
            password += times_pointed_at_zero
        string = (
            f'dial rotated {step} to point at {dial_position}; {"during this rotation, the dial pointed at zero " + str(times_pointed_at_zero) + " times" if times_pointed_at_zero > 0 else ""}'
        )
        print(string)
    return password

print(calculate_password(puzzle_input, 50))