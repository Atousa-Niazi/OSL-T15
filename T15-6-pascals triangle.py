#Atousa Niazi Abkoh - 98440127 - python - pascals_triangle - OSL - T15-6
# I use codes in https://www.codegrepper.com/code-examples/python/pascal%27s+triangle+in+python to make pascals triangle def 
# and https://www.geeksforgeeks.org/python-program-to-print-pascals-triangle/ to print it in a beautiful shape

def solve(A):
    pascals_triangle = []

    for i in range(A):
        pascals_triangle.append([1]*(i+1))
  
    for i in range(2,A):
        for j in range(1,i):
            pascals_triangle[i][j] = pascals_triangle[i-1][j-1] + pascals_triangle[i-1][j]
            
    for i in range(A):
        # adjust space
        print(' '*(A-i), end='')
     
        # compute power of 11
        print(' '.join(map(str, str(11**i))))

    return pascals_triangle

print()
n=int(input('n:'))
r=solve(n)
