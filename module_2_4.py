numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(2, 16): # или здесь можно поставить  for i in range(len(numbers) + 1)? Но тогда в расчет попадает 1(
    for n in range(2, int(i ** 0.5) + 2):
        if i % n != 0:
            primes.append(i)
            break
        else:
            not_primes.append(i)
            break
print(primes)
print(not_primes)
