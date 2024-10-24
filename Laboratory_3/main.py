import random


def separator(x):
    for i in range(x):
        if i % 2 == 0:
            print("=", end="")
        else:
            print("-", end="")
    print()


def generate_random_number():
    U = random.uniform(0, 1)
    p = [0.2, 0.4, 0.3, 0.1]
    if U <= p[0]:
        return 1
    if p[0] < U <= p[0] + p[1]:
        return 2
    if p[0] + p[1] < U <= p[0] + p[1] + p[2]:
        return 3
    if p[0] + p[1] + p[2] < U <= 1.0:
        return 4


def generate_random_numbers_with_distribution(n):
    count = [0, 0, 0, 0]
    numbers = [generate_random_number() for _ in range(n)]
    for num in numbers:
        if num == 1:
            count[0] += 1
        elif num == 2:
            count[1] += 1
        elif num == 3:
            count[2] += 1
        elif num == 4:
            count[3] += 1
    return count


def reverse_distribution():
    return random.uniform(0, 100) + 50


def generate_uniform_distribution(a, b, n):
    distribution = []
    bin_counts = [0 for _ in range(10)]
    x = [a + i * ((b - a) / 10) for i in range(10)]
    for _ in range(n):
        u = reverse_distribution()
        distribution.append(u)
        bin_counts[int((u - a) // ((b - a) / 10))] += 1
    print("\t>> Output:")
    for i in range(10):
        print("\t\t>>", x[i], "->", bin_counts[i])


def main():
    x = 135
    n = 100000
    a = 50
    b = 150
    print()
    separator(x)
    print("[INFO] LABORATORY 3 - RANDOM NUMBER GENERATORS WITH ARBITRARY DISTRIBUTION")
    separator(x)
    print("[INFO] 1. Method of inverting the distribution function for 100000 random numbers:")
    count = generate_random_numbers_with_distribution(n)
    print("\t>> Input:")
    print("\t>> x = 1   | 2   | 3   | 4")
    print("\t>> y = 0.2 | 0.4 | 0.3 | 0.1")
    print("\t\t>> Output/Number of occurrences:")
    print("\t\t>> 1: ", count[0])
    print("\t\t>> 2: ", count[1])
    print("\t\t>> 3: ", count[2])
    print("\t\t>> 4: ", count[3])

    separator(x)
    print("[INFO] 2. Generating Uniform Distribution:")
    generate_uniform_distribution(a, b, n)


if __name__ == '__main__':
    main()