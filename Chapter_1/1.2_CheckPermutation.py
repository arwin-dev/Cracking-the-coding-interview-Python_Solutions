from collections import Counter

def CheckPermutation(string1,string2):


    if len(string1) != len(string2):
        return False
    
    counter = Counter()
    for a in string1:
        counter[a] += 1
    for b in string2:
        if counter[b] == 0:
            return False
        counter[b] -= 1
    return True

print(CheckPermutation('dcw4f', 'dcwf'))