def all_variants(text):
    length = len(text)

    for k in range(1, length + 1):
        for j in range(length - k + 1):
            yield text[j: j + k]


a = all_variants("abc")
for i in a:
    print(i)
