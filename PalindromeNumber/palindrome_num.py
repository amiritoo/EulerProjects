reverse_num= 0
for i in range(10,1000):
    for j in range(10,1000):
        number= i*j
        original_num= number
        reverse_num= 0
        while(number!=0):
            r= number % 10
            reverse_num = reverse_num *10 + r
            number= number//10
        if(original_num==reverse_num):
            print(original_num)

    


