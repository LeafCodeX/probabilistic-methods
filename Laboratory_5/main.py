with open('data.txt', 'r') as f:
    data = [float(line.strip().replace(',', '.')) for line in f]

n = len(data)
mean = sum(data) / n
moment1 = mean
moment2 = sum(x**2 for x in data) / n
moment_central1 = sum((x - mean) for x in data) / n
moment_central2 = sum((x - mean)**2 for x in data) / n
std_dev = (moment_central2) ** 0.5
mean_dev = sum(abs(x - mean) for x in data) / n
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print(f'>> [INFO] Obliczanie momentów statystycznych:')
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print(f'>> Moment zwykły 1 rzędu: {round(moment1, 4)}')
print(f'>> Moment zwykły 2 rzędu: {round(moment2, 4)}')
print(f'>> Moment centralny 1 rzędu: {moment_central1}')
print(f'>> Moment centralny 2 rzędu: {round(moment_central2, 4)}')
print(f'>> Odchylenie standardowe: {round(std_dev, 4)}')
print(f'>> Średnie odchylenie od średniej: {round(mean_dev, 4)}')
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")