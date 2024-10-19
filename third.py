def je_prvocislo(cislo):
    """
    Funkce overi zda je cislo prvocislo.
    """
    num = int(cislo)                            #prevod z any type na int type pro logicke operace
    if num <= 1:
        return None
    else:                                       #overeni pokud je cislo delitelne pouze cislem 1 a samym sebou
        overeni = None
        for i in range(2, num):                 #pro kazde i (cislo) v rozmezi 2 a num
            if (num % i) == 0:                      #pokud num % i == 0 | pokud num / i vyslo bez zbytku
                overeni = True                  # overeni = true, cislo je delitelne vicekrat nez pouze cislem 1 a samym sebou
                break
        if overeni == True:                     #pokud je overeni = true,
            return False                            #a) fce je_prvocislo vraci False protoze dane cislo je prvocislo.
        else:
            return True                             #b) fce je_prvocislo vraci True protoze dane cislo je prvocislo.

def vrat_prvocisla(maximum):
    """
    Funkce spocita vsechna prvocisla v rozsahu 1 az maximum a vrati je jako seznam.
    """
    results = []
    cisla = list(range(1, int(maximum) + 1))    # vytvoreni listu "cisla" od (1;maximum>

    for item in cisla:                          #for overi pro kazde cislo v listu, zda je prvocislo
        if je_prvocislo(item) == True:          #                                   pomoci fce je_prvocislo(cislo),
            results.append(item)                #pokud je fce je_prvocislo(cislo) = True, zapise do listu results 
    return results                              #fce vrat_prvocisla(maximum) vraci list results

if __name__ == "__main__":
    cislo = je_prvocislo(100)
    print (cislo)
    cislo = input("Zadej maximum: ")
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)