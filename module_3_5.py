def gmd(number):
    str_number = str(number)
    first = int(str_number[0])
    ttt = len(str_number)
    if ttt > 1:
        first =  first * gmd(int(str_number[1:]))
        return first
    else:
        return first
print(gmd(285))
