def isPalindrome(word): 
    list1= word.split(" ")
    for i in range(0, int(len(word)/2)):  
        if word[i] != word[len(word)-i-1]: 
            return False
    return True

word = input("ur word: ")
answer = isPalindrome(word) 
  
if (answer): 
    print("Yes") 
else: 
    print("No") 

