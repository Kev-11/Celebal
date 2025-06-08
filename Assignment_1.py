def lower_triangle(n):
    print("Lower Traingle:")
    for i in range(1,n+1):
        print('*'*i)
    print('\n')

def upper_triangle(n):
    print("Upper Traingle:")
    for i in range(n,0,-1):
        print('*'*i)
    print('\n')
def pyramid(n):
    print("Pyramid:")
    for i in range(1,n+1):
        print(" "*(n-i)+"*"*(2*i-1))

try:
    n = int(input())
except:
    print("Please enter a number.") # I have used try and except here incase the input is not numeric(integer)
    exit()

lower_triangle(n)
upper_triangle(n)
pyramid(n)