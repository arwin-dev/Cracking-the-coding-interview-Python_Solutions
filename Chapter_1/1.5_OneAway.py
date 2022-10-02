from re import L


from collections import Counter
def OneAway(string1,string2):
    if len(string2) > len(string1):
        string1,string2 = string2,string1

    counter = Counter()
    sum = 0
    for i in string1:
        counter[i] += 1
        sum += 1
    
    print(counter)
    
    for j in string2:
        counter[j] -= 1
        if j in string1:
            sum -= 1
    
    print(counter)
    print(sum)

    return True if sum <= 1 else False

print(OneAway('palks', 'pal'))