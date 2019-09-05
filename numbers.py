num = 10

while num < 100:
    first = num // 10
    second = num % 10
    if (first + second)**2 == num:
        print(num)
    num += 1

num = 1
devisors = 0
while num < 100:
    for n in range(1, num + 1):
        if num % n == 0:
            devisors += 1
    if devisors == 10:
        print (num)
    num += 1
    devisors = 0
