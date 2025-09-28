from array import array

primes = array('i', [2,3,4,5,6,7,8,9])

# The typecodes supported are based on c data types

print(primes)
print(primes[0])

primes.extend([2, 3, 4])

print(primes)

print(len(primes))