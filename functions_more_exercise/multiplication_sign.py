def multiplication(num1, num2, num3):
    if num1 < 0 or num2 < 0 or num3 < 0:
        return "negative"
    elif num1 > 0 and num2 > 0 and num3 > 0:
        return "positive"
    elif num1 == 0 or num2 == 0 or num3 == 0:
        return "zero"


number1=int(input())
number2=int(input())
number3=int(input())
print(multiplication(number1,number2,number3))
