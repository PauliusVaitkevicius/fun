"""
Inverting a string
"""

from timeit import default_timer as timer

s = "I will invert you!"
print(s)

# The most elegant and pythinic way:
# Execution time: 9.049999999954927e-07
start_time = timer()
s_inv = s[::-1]
end_time = timer()
print("\nPythonic")
print(s_inv)
print("Done in: {}".format(end_time - start_time))

# A "thinking it step by step" way:
# Execution time: 1.3668000000001401e-05
start_time = timer()
s_inv = ""
for idx, letter in enumerate(s, start=1):
    s_inv += s[len(s) - idx]
end_time = timer()
print("\nClassic")
print(s_inv)
print("Done in: {}".format(end_time - start_time))
