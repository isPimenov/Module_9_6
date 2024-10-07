def all_variants(text):
    l = len(text)
    for n in range(1, l+1):
        i = 0
        while i <= l - n:
            yield text[i:i+n]
            i += 1


a = all_variants("abc")
for i in a:
    print(i)

