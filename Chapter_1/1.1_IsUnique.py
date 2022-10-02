def IsUnique(string):
    if len(string) > 128:
        return False
    
    HashMap = {}
    for char in string:
        val = ord(char)
        if val in HashMap:
            return False
        HashMap[val] = char
        print(HashMap)
    return True

print(IsUnique('abcdd'))
