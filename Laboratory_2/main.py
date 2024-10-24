import time
import math


class LinearGenerator:
    def __init__(self, A, C, M, seed):
        self.A = A
        self.C = C
        self.M = M
        self.previous = seed % self.M

    def next(self):
        self.previous = (self.A * self.previous + self.C) % self.M
        return self.previous / self.M


class ShiftRegisterGenerator:
    def __init__(self, P, Q, seed: int = 0b101010101010101010):
        self.p = P
        self.q = Q
        self.seed = seed

    def next(self):
        new_bit = (self.seed >> (self.p - 1)) ^ (self.seed >> (self.q - 1))
        new_bit &= 1
        self.seed = ((self.seed << 1) | new_bit) & ((1 << self.p) - 1)
        return new_bit


def separator(x):
    for i in range(x):
        if i % 2 == 0:
            print("=", end="")
        else:
            print("-", end="")
    print()


def print_intervals(gen):
    intervals = [0] * 10
    for num in gen:
        index = int(num * 10)
        intervals[index] += 1
    for i in range(10):
        print(f"\t\t>> ({i / 10:.1f}, {(i + 1) / 10:.1f}): {intervals[i]}")


def calculate_area(gen, it, r):
    counter = 0
    for i in range(0, len(gen), 2):  # we use two elements from gen for each iteration
        if i + 1 >= len(gen):  # if no pair for the last element, break the loop
            break
        x = gen[i] * 2
        y = gen[i + 1] * 2
        if math.sqrt((x - 1) ** 2 + (y - 1) ** 2) <= 1:
            if math.sqrt((x - 2) ** 2 + (y - 2) ** 2) <= r:
                counter += 1
    area = counter / it * 4
    print("\t>> The area of overlapping circles: ", area)


def count_bits_in_gen(gen):
    count_1 = sum(gen)
    count_0 = len(gen) - count_1
    return count_0, count_1


def calculate_probability(shift_register_generator, N, K, i):
    probability = 0
    for _ in range(i):
        count = 0
        for _ in range(N):
            val = shift_register_generator.next()
            if val:
                count += 1
            else:
                count = 0
            if count == K:
                probability += 1
                break
    probability /= i
    return probability


if __name__ == '__main__':
    A = 16807
    C = 0
    M = 2 ** 31 - 1
    N = 10000

    P = 10
    Q = 3

    x = 135
    print()
    separator(x)
    print("[INFO] LABORATORY 2 - PSEUDO-RANDOM NUMBER GENERATORS")
    separator(x)
    print("[INFO] 1. Linear Congruential Generator:")
    linear_generator = LinearGenerator(A, C, M, int(time.time()))
    gen_l = []
    print("\t>> [", end='')
    for i in range(N):
        num = linear_generator.next()
        gen_l.append(num)
        if i == N - 1:
            print(f"{round(num, 4)}", end='')
        else:
            print(f"{round(num, 4)}, ", end='')
    print("]")
    print("\t>> Mean:", round(sum(gen_l) / N, 4))
    print("\t\t>> Intervals:")
    print_intervals(gen_l)
    print("[INFO] 1D. Calculating the area of a circle:")
    calculate_area(gen_l, N, 1)
    separator(x)
    print("[INFO] 2. Shift Register Generator:")
    shift_register_generator = ShiftRegisterGenerator(P, Q)
    gen_r = []
    print("\t>> [", end='')
    for i in range(N):
        num = shift_register_generator.next()
        gen_r.append(num)
        if i == N - 1:
            print(f"{round(num, 4)}", end='')
        else:
            print(f"{round(num, 4)}, ", end='')
    print("]")
    print("\t>> Mean:", round(sum(gen_r) / N, 4))
    count_0, count_1 = count_bits_in_gen(gen_r)
    print("\t\t>> Number of 0s in gen:", count_0)
    print("\t\t>> Number of 1s in gen:", count_1)

    print("[INFO] 2D. Counting the number of sequences:")
    N2 = 20
    K = 5
    i = 10000
    probability = calculate_probability(shift_register_generator, N2, K, i)
    print(f"\t>> The probability of the sequence of {K} ones in {N2} throws is {probability}.")
    print(f"\t>> Data: N = {N2}, K = {K}, i = {i} (iterations).")
    separator(x)