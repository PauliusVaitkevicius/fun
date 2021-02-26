"""
"Write a program that prints the numbers from 1 to 100.
But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
For numbers which are multiples of both three and five print “FizzBuzz”."
"""

import time
from timeit import default_timer as timer

"""Simple and clean way:"""
start_time = timer()
fizzbuzz = ""
for i in range(1, 101):
    # if (i % 3 == 0) and (i % 5 == 0):
    if i % 15 == 0:
        fizzbuzz += " FizzBuzz"
    elif i % 3 == 0:
        fizzbuzz += " Fizz"
    elif i % 5 == 0:
        fizzbuzz += " Buzz"
    else:
        fizzbuzz += " {}".format(i)
end_time = timer()
print(fizzbuzz)
print("Done in: {}".format(end_time - start_time))


# Althouhg one could see this as a more elegant way, but it is acctually ~1.5e-05 seconcs slower :)
start_time = timer()
fizzbuzz = ""
for i in range(1, 101):
    s = ""
    s += "Fizz" if i % 3 == 0 else ""
    s += "Buzz" if i % 5 == 0 else ""
    fizzbuzz += " {}".format(s) if s else " {}".format(i)
end_time = timer()
print(fizzbuzz)
print("Done in: {}".format(end_time - start_time))
