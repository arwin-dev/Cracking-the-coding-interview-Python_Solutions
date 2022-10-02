def URLify(string):
    str = ''
    count = 0
    string = string.strip()
    l = len(string)
    for i in string:
        if i == ' ':
            i = '%20'
            count += 1
        str += i

    return str
    
print(URLify('much ado about nothing      '))

