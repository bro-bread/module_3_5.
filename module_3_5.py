def get_multiplied_digits(number):
    s = []
    h = list(str(number))
    l = len(h)
    n = 1
    for i in range(0,l):
        s.append(int(h[i]))
        n = 1
        for el in s:
            n *= el
    print(n)

get_multiplied_digits(123456789)