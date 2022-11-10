import math
import numpy

#Question:
#If we list all the natural numbers below 10 that are multiples of 3 or 5,
#we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

#Natural numbers are 0,1,2,3...
#S(n) = the set of multiples of 5 and 3 below n.

def S(n):

    Set_3 = [] #An empty list for the multiples of 3
    Set_5 = [] #An empty list for the multiples of 5

    multiple_of_3 = 0 #Initialising Variable
    multiple_of_5 = 0 #Initialising Variable

    x = 0 #Initialising Parameter for circling through multiples

    while multiple_of_3 < n:
        Set_3.insert(x, multiple_of_3)
        x = x + 1
        multiple_of_3 = 3*x

    x = 0

    while multiple_of_5 < n:
        Set_5.insert(x, multiple_of_5)
        x = x + 1
        multiple_of_5 = 5*x

    #this will combine all elements of both lists but
    #destroy all duplicates which in this case is what we want

    Set_3_and_5 = list(set(Set_3 + Set_5))

    Sum_of_Set = sum(Set_3_and_5)

    return Sum_of_Set

print(S(1000))

#Looking at other solutions to this Problem though it is clear
#that this approach is overkill and inefficinet through
#Examples of Better Code
#1)
print(sum([x for x in range(1000) if x%3==0 or x%5==0]))
#2)
x = 1000
total = 0

for n in range(1, x):
    if n%3 == 0 < x:
        total += n
    elif n%5 == 0 < x:
        total += n
    else:
        continue

print(total)
#3)
k=1
l=0
while k < 1000:
    if k%3==0 or k%5==0:
        print(k)
        l+=k
    k+=1
print(l)
