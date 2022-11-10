# Question:
# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# Answer:

# Integer sumation function
def S1(n):
    s = (n*(n+1))/2
    return s

# Squares sumation function
def S2(n):
    s = (n*(n+1)*((2*n)+1))/6
    return s

# A sumation function which
def Sum(n,p):
    if p == 1:
        return S1(n)
    elif p == 2:
        return S2(n)
    else:
        print("ERROR!")

def P2(n):
    s = (S1(n))**2
    return s

sol = abs(Sum(100, 2) - P2(100))
print(sol)
