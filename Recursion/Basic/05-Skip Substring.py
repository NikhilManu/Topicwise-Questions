# Give two strings string and sub, remove all occurences of sub

def skipString(string, sub):
    if not string:
        return ""

    if (string[0:len(sub)] == sub):
        return skipString(string[len(sub):], sub)
    else:
        return string[0] + skipString(string[1:], sub)

print(skipString("iwantanapple", "an"))