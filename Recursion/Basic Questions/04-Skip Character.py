# Given a string and skip the character 'a'

# Method 1
def skipChar1(string):
    return helper("", string)
    

def helper(cur, string):
    if not string:
        return cur
    
    if (string[0] == 'a'):
        return helper(cur, string[1:])
    else:
        return helper(cur + string[0], string[1:])
    
print(skipChar1("baccad"))

# Method 2
def skipChar2(string):
    if not string:
        return ""

    if (string[0] == 'a'):
        return skipChar2(string[1:])
    else:
        return string[0] + skipChar2(string[1:])

print(skipChar2("baccad"))