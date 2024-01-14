import math


def center_point(x1, x2, y1, y2):
    if math.floor(abs(x1) + abs(x2)) < math.floor(abs(y1) + abs(y2)):
        return f"{x1, x2}"
    elif math.floor(abs(x1)) + math.floor(abs(x2) > (abs(y1) + abs(y2))):
        return f"{y1, y2}"


x_num1 = math.floor(float(input()))
x_num2 = math.floor(float(input()))
y_num1 = math.floor(float(input()))
y_num2 = math.floor(float(input()))
print(center_point(x_num1,x_num2,y_num1,y_num2))
