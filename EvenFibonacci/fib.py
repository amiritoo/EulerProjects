first_number= 1
sec_number= 2
sum= 0

while (first_number < 4000000):
    new= first_number + sec_number
    first_number= sec_number
    sec_number= new
    if(first_number % 2== 0):
        sum= sum+first_number
print(sum)
