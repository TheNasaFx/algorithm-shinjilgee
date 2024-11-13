def count_primes(n):
    # Create an array to track prime status of numbers from 0 to n
    is_prime = [True] * (n + 1)

    # 0 and 1 are not prime numbers
    is_prime[0] = False
    is_prime[1] = False

    # Sieve of Eratosthenes
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False  # Mark multiples of p as not prime

    # Count the total number of primes
    prime_count = sum(is_prime)  # Sum of True values gives the count of prime numbers

    return prime_count  # Return the total count of prime numbers

# Example usage
n = 18
result = count_primes(n)
print(f"The number of prime numbers up to {n} is: {result}")  # Output: 7
