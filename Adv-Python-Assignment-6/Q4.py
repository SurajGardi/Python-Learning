# 4. Generators: Implement a generator function that yields prime numbers indefinitely.
# prime_generator

def prime_generator():
    num = 2
    while True:
        is_prime = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            yield num

        num += 1


def main():
    primes = prime_generator()

    for _ in range(10):   # print first 10 prime numbers
        print(next(primes))


if __name__ == "__main__":
    main()
