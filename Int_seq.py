num = 1
tot = 0
num_max = 0
even = 0
odd = 0
valid_num = 0

while num > 0:
    num = int(input("Enter an integer: "))
    if num <= 0:
        break
    valid_num = 1
    tot += num
    print("Cumulative total:", tot)
    if num > num_max:
        num_max = num
    if num % 2 == 0 and num != 0:
        even += 1
    elif num != 0:
        odd += 1

if valid_num == 1:
    print("Largest number:", num_max)
    print("Count of even numbers:", even)
    print("Count of odd numbers:", odd)
