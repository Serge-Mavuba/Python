# Lists are built-in data structure for storing and accesssing objects
# which belong in a specific sequence.
# There are 2 ways to create a list:
#   1) by using the list constructor: Example = list() 
#   2) by using brackets:             Example = []

# You can create a list and prepopulate it with values/elements
#   Consider the list PRIMES with values 2,3,5,7,11,13
PRIMES = [2,3,5,7,11,13]
print(PRIMES)
print("---------------------------------")
#The list should print as follow [2,3,5,7,11,13]

# Consider the list PRIMES with values 2,3,5,7,11,13
#  Use the "append" command to add new values 17 & 19 to the end of the list
PRIMES = [2,3,5,7,11,13]
PRIMES.append(17)
PRIMES.append(19)
print(PRIMES)
print("---------------------------------")

# Consider the list PRIMES with values 2,3,5,7,11,13
# if you want to see a specific value, you can access it by its index
# by default the 1st value of a list has an index value "0", the 2nd "1", the 3rd "2", and so forth 
PRIMES[0]
PRIMES[1]
PRIMES[2]
PRIMES[-1]
PRIMES[-8]
 
print(PRIMES[0])
print(PRIMES[1])
print(PRIMES[2])
print("---------------------------------")

# Now what if you use a negative index? For example -1. It will loop around and bring you back of the end of the list 
PRIMES[-1]
PRIMES[-8]
print(PRIMES[-1])
print(PRIMES[-8])


print("---------------------------------")

# You can access values by slicing; Slicing retrieves a range of values from a List
# List Name = [index value : index value].. Note that sclicing includes the value at the starting index
# but excludes the value of the stopping index
print(PRIMES)
PRIMES[2:5]
print(PRIMES[2:5])


