"""
Inverting a string
"""

from timeit import default_timer as timer

s = "You can also use negative index numbers to slice a string. As we went through before, negative index numbers of a string start at -1, and count down from there until we reach the beginning of the string."
print(s)

# The most elegant and pythinic way:
# Execution time: 1.6610000000000236e-06
start_time = timer()
s_inv = s[::-1]
end_time = timer()
print("\nPythonic")
print(s_inv)
print("Done in: {}".format(end_time - start_time))

# A "thinking it step by step" way:
# Execution time: 7.548300000000119e-05
start_time = timer()
s_inv = ""
for idx, letter in enumerate(s, start=1):
    s_inv += s[len(s) - idx]
end_time = timer()
print("\nClassic")
print(s_inv)
print("Done in: {}".format(end_time - start_time))


# Even more low-level thinking way:
# I cant believe it's the fastest way
# Execution time: 5.9702000000001754e-05
start_time = timer()
start = 0
end = len(s) - 1
s_inv = ""
while end >= start:
    s_inv += s[end - start]
    start += 1
end_time = timer()
print("\nClassic - fasest")
print(s_inv)
print("Done in: {}".format(end_time - start_time))
