import csv
import math


class City:
    def __init__(self, id, name, population, latitude, longitude):
        self.id = id
        self.name = name
        self.population = population
        self.latitude = latitude
        self.longitude = longitude


def distance(city1, city2):
    lat1, lon1 = city1.latitude, city1.longitude
    lat2, lon2 = city2.latitude, city2.longitude
    return math.sqrt((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2)


def total_distance(path):
    return sum(distance(path[i], path[i + 1]) for i in range(len(path) - 1)) + distance(path[0], path[-1])


def shortest_path(cities, K):
    all_paths = variations_without_repeats(cities, K)
    shortest = min(all_paths, key=total_distance)
    return shortest, total_distance(shortest)


def variations_without_repeats(list, n):
    if n == 0:
        return [[]]
    generated_list = []
    for i in range(len(list)):
        m = list[i]
        copy_list_no_m = list[:i] + list[i + 1:]  # copy list without m
        for j in variations_without_repeats(copy_list_no_m, n - 1):
            generated_list.append([m] + j)  # append m to the rest of the list and return variation from copy_list_no_m
    return generated_list


def area_of_cities(cities):
    min_lat = min(city.latitude for city in cities)
    max_lat = max(city.latitude for city in cities)
    min_lon = min(city.longitude for city in cities)
    max_lon = max(city.longitude for city in cities)
    return (max_lat - min_lat) * (max_lon - min_lon)


def smallest_area(cities, K):
    all_combinations = combinations(cities, K)
    smallest = min(all_combinations, key=area_of_cities)
    return smallest, area_of_cities(smallest)


def combinations(list, n):
    if n == 0:
        return [[]]
    generated_list = []
    for i in range(len(list)):
        m = list[i]
        copy_list = list[i + 1:] # copy without current and previous elements
        for j in combinations(copy_list, n - 1):
            generated_list.append([m] + j)
    return generated_list


def main():
    cities = []
    with open('data.csv', 'r') as file:
        reader = csv.reader(file, delimiter=' ')
        next(reader)
        for row in reader:
            if len(row) == 5:
                id, name, population, latitude, longitude = row[0], row[1], int(row[2]), float(row[3]), float(row[4])
                cities.append(City(id, name, population, latitude, longitude))
            else:
                print(f"Skipping row due to insufficient columns: {row}")

    print("\n[INFO] LABORATORY 1 - VARIATIONS AND COMBINATIONS\n", end="")

    N = int(input("Enter max number (N): "))
    K = int(input("Enter size (K): "))

    if K > N:
        print("Size of the variation cannot be greater than the maximal number.")
        return

    print("\n[INFO] 1. Variations without repeats:")
    variations = variations_without_repeats([city.id for city in cities[:N]], K)
    for i, variation in enumerate(variations, start=1):
        if i <= 25:
            print(f"{i}: {list(variation)}")
        elif i == 26:
            print("And more...")
            break

    print(f"[TOTAL] {len(variations)} variations")

    print("\n[INFO] 1D. Shortest path/cycle:")
    #path, total_distance = shortest_path(cities[:N])
    path, total_distance = shortest_path(cities[:N], K)
    print(f"Distance (cycle) is: {total_distance}")
    print(f"Path for shortest distance: {', '.join([city.name for city in path])}")

    print("\n[INFO] 2. Combinations: ")
    all_combinations = combinations([city.id for city in cities[:N]], K)
    for i, combination in enumerate(all_combinations, start=1):
        if i <= 25:
            print(f"{i}: {list(combination)}")
        elif i == 26:
            print("And more...")
            break
    print(f"[TOTAL] {len(all_combinations)} combinations")

    print("\n[INFO] 2D. Smallest area:")
    subset, area = smallest_area(cities[:N], K)
    print(f"Smallest area: {area}")
    print(f"Path: {', '.join([city.name for city in subset])}")


if __name__ == "__main__":
    main()

    # def variations_with_repeats(lst, n):
    #    if n == 0:
    #        return [[]]
    #    l = []
    #    for m in lst:
    #        for p in variations_with_repeats(lst, n-1):
    #            l.append([m] + p)
    #    return l

    # print("[INFO] Variations with repeats")
    # variations = variations_with_repeats([city.id for city in cities[:N]], K)
    # for i, variation in enumerate(variations, start=1):
    #    print(f"{i}: {list(variation)}")
    # print(f"Total {len(variations)} variations")
