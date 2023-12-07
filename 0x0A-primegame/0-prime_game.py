#!/usr/bin/python3
"""Prime Game module"""


def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_all_primes(n):
    """Get all prime numbers up to n"""
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def isWinner(x, nums):
    """Determine the winner of the prime game"""
    if x <= 0 or not nums:
        return None

    wins = {"Maria": 0, "Ben": 0}

    for n in nums:
        primes = get_all_primes(n)
        total_primes = len(primes)
        # If the total number of primes is even, Ben wins; otherwise, Maria wins
        winner = "Ben" if total_primes % 2 == 0 else "Maria"
        wins[winner] += 1

    # Determine the player with the most wins
    if wins["Maria"] == wins["Ben"]:
        return None
    return max(wins, key=wins.get)


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
