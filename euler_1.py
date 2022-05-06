# just some fun euler questions to keep my brain moving


def three_five(n):
    sum = 0
    for i in range(3, n):
        if i %3 == 0 or i%5 == 0:
            sum += i
    return sum

def fib_numbers_even(n):
    val1, val2 = 1, 2
    val = 0
    even_sum = 2
    while val < n:
        if val % 2 == 0:
            even_sum += val
        val = val1 + val2
        val1 = val2
        val2 = val
    return even_sum

def isPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    end = int(n**(1/2))
    for i in range(2, end + 1):
        if n % i == 0:
            return False
    
    return True

def largest_prime_factor(n):
    root = int(n**(1/2))
    for i in  range(root+1, 2, -1):
        if n % i == 0 and isPrime(i):
            return i
    return -1

def isPalinedrome(n):
    num = list(str(n))
    nl = len(num)
    for i in range(int(nl/2)):
        if num[i] != num[nl-1-i]:
            return False
    return True

def largest_palindrome(n):
    top = 10**n-1

    max = 0
    second = top
    for i in range(top, 1, -1):
        # print(i, curr_prod, second)
        for j in range(second, 1, -1):
            curr_prod  = i*j
            if isPalinedrome(curr_prod):
                if curr_prod > max: max = curr_prod
        second -= 1
    return max

def smallest_multiple(n):
    valid = False
    common = 0
    while not valid:
        common += 1

        valid = True
        for i in range(2, n+1):
            if common % i != 0:
                valid = False


    return common

def smallest_multiple_smart(n):
    common = 1
    for i in range(2, n+1):
        if isPrime(i):
            common *= i
        else:
            m_factor = 1
            while common % i != 0:
                m_factor += 1
                if i % m_factor == 0:
                    common *= m_factor
    return common

def ss_diff(n):
    sum = 0
    sum2 = 0
    for i in range(1, n+1):
        sum += i**2
        sum2 += i
    return abs(sum - sum2**2)


def main():
    print(ss_diff(100))

if __name__ == '__main__':
    main()