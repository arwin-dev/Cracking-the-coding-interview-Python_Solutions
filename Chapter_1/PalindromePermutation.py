from collections import Counter
def Palindrome(string):
    counter = Counter()
    string = string.lower().replace(' ','')
    for i in string:
        counter[i] += 1
    
    sum = 0
    print(counter)
    for i in string:
        sum += counter[i] % 2
        print(sum)
    
    return True if sum <= 1 else False


print(Palindrome('azAZ'))