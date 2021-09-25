def t_gen(row, direction):
    while row:
        row += direction 
        yield (row**2 + row) // 2, (row + 1) * (row + 2) // 2


def max_sum(t, f):
    lines = len(t)
    for (s, e), i  in zip(t_gen(lines - 1, -1), range(lines - 1, 0, -1)):
        gap = e - s
        for i in range(s - gap + 1, e - gap):
            f[i] += max(f[i + gap - 1], f[i + gap])
    return f[0] 


triangle = '''              
                            75
                          95  64
                        17  47  82
                      18  35  87  10
                    20  04  82  47  65
                  19  01  23  75  03  34
                88  02  77  73  07  63  67
              99  65  04  28  06  16  70  92
            41  41  26  56  83  40  80  70  33
          41  48  72  33  47  32  37  16  94  29
        53  71  44  65  25  43  91  52  97  51  14
      70  11  33  28  77  73  17  78  39  68  17  57
    91  71  52  38  17  14  91  43  58  50  27  29  48
  63  66  04  68  89  53  67  30  73  16  69  87  40  31
04  62  98  27  23  09  70  98  73  93  38  53  60  04  23
'''.split('\n')[1:]
t = [[int(n) for n in line.split()] for line in triangle]
f = [int(n) for line in triangle for n in line.split()]

print(max_sum(t, f))

