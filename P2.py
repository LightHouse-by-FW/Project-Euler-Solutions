import math

#Question:
#Each new term in the Fibonacci sequence is generated by adding the previous
#two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed
#four million, find the sum of the even-valued terms.

#A function which generates the nth Fibonacci number
def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

#A function which generates a list of all Fibonacci numbers
#below n, finds the even members and then sums them
def Fibonacci_Sum_Below(n):

    Fibonacci_Terms_Set = [] #empty set
    x = 0 #A counter so that we can keep adding to our set
    current = 0 #The current Fibonacci number in the while loop
                #so that the loop stops at n

    #Loop to create our list
    while current < n:
        current = Fibonacci(x + 1)
        Fibonacci_Terms_Set.insert(x, current)
        x = x + 1
        current = Fibonacci(x + 1) #Put it in a second time so that
                                   #does not exceed 4,000,000

    #Getting only even Fibonacci numbers in or list
    #by first making a set of the index numbers where
    #the Fibonacci number is not even.
    Fibonacci_Non_Even = []
    x = 0 #A counter for the index in the if statement
    for i in range(0,len(Fibonacci_Terms_Set)):
        if Fibonacci_Terms_Set[i] % 2 == 1:
            Fibonacci_Non_Even.insert(x, i)
            x = x + 1

    #Now that we have the list of indicies we want deleted we will
    #preform the deleting backwards since that way we don't have the
    #problem of higher index values we want being removed when the
    #lower ones are deleted.

    for i in sorted(Fibonacci_Non_Even, reverse=True):
        del Fibonacci_Terms_Set[i]

    #We now have a set with only Even Fibonacci numbers
    #and so now we sum the set to give our answer
    return sum(Fibonacci_Terms_Set)

print(Fibonacci_Sum_Below(4000000))

#Sadly this code is also slightly in efficient and so I will
#Once again be presenting with solutions found by others which are interesting
#and more efficient
#1)
'''[b]Begoner[/b] said
[quote]This may be a small improvement.  The Fibonacci series is:

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610...

Now, replacing an odd number with O and an even with E, we get:

O, O, E, O, O, E, O, O, E, O, O, E, O, O, E...

And so each third number is even.  We don't need to calculate the odd numbers.  Starting from an two odd terms x, y, the series is:

x, y, [b]x + y[/b], x + 2y, 2x + 3y, [b]3x + 5y[/b]

And in Python, my solution is:

[code=Python]def calcE():'''
	x = y = 1
	sum = 0
	while (sum < 1000000):
		sum += (x + y)
		x, y = x + 2 * y, 2 * x + 3 * y
	return sum[/code]

#With this, you don't need to use an % to calculate if a number is even.  Using a fast computer, this took less than 0.01 secs to calculate.
#[/quote]
#2)
'''[b]RudyPenteado[/b] said
[quote]I estimate that I had written about 3 million lines
 of assembler code in my whole life. Now, code only
 when strictly necessary.

Phi (golden ratio) is the approximate ratio between
 two consecutive terms in a Fibonacci sequence.
The ratio between consecutive even terms approaches
 phi^3 (4.236068) because each 3rd term is even.
Use a calculator and round the results to the nearest
 integer when calculating the next terms:

 2,8,34,.. multiplying by 4.236068 each time: 144,610,
 2584,10946,46368,196418 & 832040

The sum is 1089154

My codeless regards,
Rudy.
[/quote]'''
#3)whitevu Solution
#VARIABLE INITIALIZATION
even_sum = 0
current_number = 2
previous_number = 1
###

while current_number < 1000000:
    if not (current_number % 2):
        even_sum += current_number
    temp = previous_number
    previous_number = current_number
    current_number += temp

print even_sum