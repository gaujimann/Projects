n = int(input("Enter the length of the sequence: "))
new_num = 0
current_num = 3
prev_num1 = 2
prev_num2 = 1

print(prev_num2)
print(prev_num1)

for i in range(3, n + 1):
    print(current_num)
    new_num = current_num + prev_num1 + prev_num2
    prev_num2 = prev_num1
    prev_num1 = current_num
    current_num = new_num
    
    
