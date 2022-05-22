
# generates prime numbers and concatenates them in a string
# until the length exceeds 10000
def generatePrimes():
    primesStr = "2"
    primes = []
    primes.append(2)
    i = 3
    while len(primesStr) < 10005:
        isPrime = True
        for j in primes:
            if i % j == 0:
                isPrime = False
        
        if isPrime:
            primes.append(i)
            nextPrime = str(i)
            primesStr += nextPrime
        i = i + 1

    return primesStr 

def solution(i):
    # Your code here
    k = i + 5
    primes = generatePrimes()
    id = ""
    for j in range(i,k):
        id += primes[j]
    return id


## Testing the code 
#print(generatePrimes())
print(solution(0))
print(solution(3))
print(solution(98))