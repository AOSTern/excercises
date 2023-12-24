def egg_count(display_value):
    count = -1
    output = []
    while display_value >= 2:
        output[:count] = [(display_value % 2)]
        display_value = display_value // 2
        count = count - 1
    output[:count] = [(display_value)]
    return sum(output)
