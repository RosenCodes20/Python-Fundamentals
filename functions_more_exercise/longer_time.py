import math


def lines(x1, x2, y1, y2, t1, t2, z1, z2):
    sum_of_x = math.floor(abs(x1) + abs(x2))
    sum_of_y = math.floor(abs(y1) + abs(y2))
    sum_of_t = math.floor(abs(t1) + abs(t2))
    sum_of_z = math.floor(abs(z1) + abs(z2))
    first_lines = math.floor(abs(sum_of_x) + abs(sum_of_y))
    second_lines = math.floor(abs(sum_of_t) + abs(sum_of_z))
    if first_lines > second_lines:
        if abs(x1) + abs(x2) > abs(y1) + abs(y2):
            return f"{y1, y2}{x1, x2}"
        else:
            return f"{x1, x2}{y1, y2}"
    elif first_lines < second_lines:
        if abs(t1) + abs(t2) > abs(z1) + abs(z2):
            return f"{z1, z2}{t1, t2}"
        else:
            return f"{t1, t2}{z1, z2}"
    else:
        if abs(t1) + abs(t2) > abs(z1) + abs(z2):
            return f"{z1, z2}{t1, t2}"
        else:
            return f"{t1, t2}{z1, z2}"


number_of_x = math.floor(float(input()))
number_of_x2 = math.floor(float(input()))
number_of_y = math.floor(float(input()))
number_of_y2 = math.floor(float(input()))
number_of_t = math.floor(float(input()))
number_of_t2 = math.floor(float(input()))
number_of_z = math.floor(float(input()))
number_of_z2 = math.floor(float(input()))
print(lines(number_of_x, number_of_x2, number_of_y, number_of_y2, number_of_t, number_of_t2, number_of_z, number_of_z2))
