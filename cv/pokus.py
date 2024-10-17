#funkce, ktera vypise do konole Hello world
import array


def hello_world():          
    print("Hello world")

hello_world()

#funkce, ketra vypise pozadovany pocet hvezd
def five_stars(limit):
    i = 0
    while i < limit:
        print('*')
        i += 1    

#funkce, ktera overi zda je number v rozmezi minimum - maxium a vypise textovy vystup
def in_range(num, min, max):
    if num > min and num < max:
        print("Number", num, "is in range", min, "-", max)
    else:
        print("Number", num, "is out of range", min, "-", max)
        


#in_range(1, 100, 1000)
#"Number 1 is out of range 100 - 1000"
#in_range(500, 100, 1000)
#"In range"

#funkce vrati nejvetsi cislo z a, b, c
def max_num(a,b,c):

    if a > b and a > c:
        return a
    if b > c and b > a:
        return b

    return c

max_num(1, 2, 3)
#3
max_num(100,10,1)
#100
max_num(1.1, 1.3, 1.2)
#1.3
