def translate(number):
    t1 = 'zero one two three four five six seven eight nine ten eleven twelve \
         thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
    t2 = 'twenty thirty forty fifty sixty seventy eighty ninety'.split()
    d = {k: v for k, v in zip(range(20), t1)} |\
        {k: v for k, v in zip(range(20, 91, 10), t2)} |\
        {100: 'hundred', 1000: 'thousand'}
    if number <= 20:
        return len(d[number])
    si, s, trns = [int(n) for n in str(number)], str(number), []
    for i, n in enumerate(si):
        digit, r = n * 10**len(s[i + 1:]), s[i + 1:]
        if digit >= 100:
            trns += [d[n]] + [d[digit / n]] + (['and'] if int(r) else [])
        elif digit >= 10:
            trns += [d[digit]] if n != 1 else [d[digit + si[i + 1]]]
        elif n != 0:
            trns += [d[n]] if si[i - 1] != 1 else []
    return len(''.join(trns))


length = 0
for i in range(1, 1001):
    length += translate(i)
print(length)
