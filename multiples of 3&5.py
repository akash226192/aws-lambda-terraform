def sumOfMultiples(param):
    sum = 0
    for i in range(param):
        if (i % 3 ==0) or (i % 5 == 0):
            sum = sum+i
    print(sum)
    return sum

