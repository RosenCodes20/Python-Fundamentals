def tribonacci(number):
    list = [1, 0, 0]
    for num in range(number):
        other_num = sum(list)
        print(other_num,end=" ")
        list.append(other_num)
        list.pop(0)


n = int(input())
tribonacci(n)
