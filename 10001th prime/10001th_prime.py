
number= 1
i=1
while(i<100002):
    for j in range(1,number//2 +1):
        if (number % j==0):
            i+=1
            number+=1
        else:
            number+=1
print(number)