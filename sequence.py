n = int(input("Enter the length of the sequence: "))
new_num = 0
current_num = 1
prev_num = 1

for i in range(1, n + 1):
    print(current_num)
    new_num = current_num + prev_num
    prev_num = current_num
    current_num = new_num
    
    
