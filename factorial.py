nr_fact = int(input('introduce un numar:'))
prod = 1
x = 2
while x <= nr_fact:
    prod *= x
    x += 1
print(prod)
nr_prod = str(prod)
print(len(nr_prod))