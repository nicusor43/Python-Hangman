from random import randint
nr_calc = randint(1,100)
while nr_calc % 2 == 1:
    nr_calc = randint(1,100)
nr_introdus = int(input('Introduce un numar de la 1 la 100: '))
while nr_introdus != nr_calc:
    if nr_introdus < nr_calc:
        print("numarul este mai mare")
    else:
        print('numarul e mai mic')
    nr_introdus = int(input('Introduce alt numar de la 1 la 100: '))
if nr_introdus == nr_calc:
    print('Numarul e corect')

