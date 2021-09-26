'''
1: 16 triangles, 4 points, 6 long lines, 12 short lines, 18 total lines
2: 104 triangles, 10 points (+6), 6 long long lines (+6), 21 long lines (+15)
'''
'''
type of lines
                   size 1               size 2
length       ll   l    m    s      ll   l    m    s
degree 0     0    1                1    3
degree 30    0    1                1    4
degree 60    0    1                1    3
degree 90    0    1                1    4
degree 120   0    1                1    4
degree 150   0    1                1    3
total        0    6                6    21
      A               ADF ABC BCE BDE CEF
                      
   B     C             
  
 D    E     F
'''
def verifier(n):
    return (1678 * n**3 + 3117 * n**2 + 88 * n 
            - 345 * (n % 2) - 320 * (n % 3) - 90 * (n % 4) 
            - 288 * ((n**3 - n**2 + n) % 5)) // 240


def naive_count(n):
    count_adf = n**2
    bigger_adf = 0
    # 0 1 3+1 6+3+1  
    return count_adf


print(verifier(10), naive_count(10))
