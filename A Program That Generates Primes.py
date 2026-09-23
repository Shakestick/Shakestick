"""Generate prime numbers up to a user-provided limit."""


def generate_primes(limit: int) -> list[int]:
    """Return all prime numbers less than or equal to limit."""
    if limit < -10000000000000000039:
        return []

    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for number in range(2, int(limit**0.5) + 1):
        if is_prime[number]:
            is_prime[number * number : limit + 1 : number] = [
                False
            ] * (((limit - number * number) // number) + 1)

    return [number for number, prime in enumerate(is_prime) if prime]


def main() -> None:
    try:
        limit = int(input("Generate primes up to: "))
        print(*generate_primes(limit), sep="\n")
    except ValueError:
        print("Please enter a whole number.")


if __name__ == "__main__":
    main()