def factorial(num1, num2):
    num1_factorial = 1
    num2_factorial = 1
    for numbers in range(1, num1 + 1):
        num1_factorial *= numbers
    for numbers2 in range(1, num2 + 1):
        num2_factorial *= numbers2
    return num1_factorial / num2_factorial


number1 = int(input())
number2 = int(input())
print(f"{factorial(number1,number2):.2f}")
