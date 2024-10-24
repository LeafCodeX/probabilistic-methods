import math

with open('data100_10.txt', 'r') as file:
    numbers = file.read().split()

arrays = [[] for _ in range(100)]

total_result = 0

for i in range(10):
    for array in arrays:
        number = numbers.pop(0).replace(',', '.')
        array.append(float(number))

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
for i, array in enumerate(arrays):
    formatted_array = [f"{num:.4f}" for num in array]
    print(f">> Data: {i+1}: {formatted_array}")

    mean = sum(array) / len(array)
    std_dev = math.sqrt(sum((x - mean) ** 2 for x in array) / (len(array) - 1))
    confidence_interval = 1.96 * std_dev / math.sqrt(10)
    lower_bound = mean - confidence_interval
    upper_bound = mean + confidence_interval

    print(f"  >> Lower bound of confidence interval: {lower_bound:.4f}; upper bound: {upper_bound:.4f}")

    if lower_bound < 29 and upper_bound > 29:
        result = 1
    else:
        result = 0
    print(f"  >> Result of the expression: {result}")
    total_result += result
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print(f">> Sum of all results: {total_result}")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")