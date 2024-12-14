def cesta_volna(start, cil, obsazena_pole):
    x_start, y_start = start
    x_cil, y_cil = cil

    if x_start == x_cil:  # Vertikální pohyb
        step_y = 1 if y_cil > y_start else -1
        for y in range(y_start + step_y, y_cil, step_y):
            if (x_start, y) in obsazena_pole:
                return False
        return True

    elif y_start == y_cil:  # Horizontální pohyb
        step_x = 1 if x_cil > x_start else -1
        for x in range(x_start + step_x, x_cil, step_x):
            if (x, y_start) in obsazena_pole:
                return False
        return True

    elif abs(x_cil - x_start) == abs(y_cil - y_start):  # Diagonální pohyb
        step_x = 1 if x_cil > x_start else -1
        step_y = 1 if y_cil > y_start else -1
        x, y = x_start + step_x, y_start + step_y
        while (x, y) != (x_cil, y_cil):
            if (x, y) in obsazena_pole:
                return False
            x += step_x
            y += step_y
        return True
    return True  # Pokud se nejedná o přímou cestu, je automaticky volná

def overeni_mimo_hraci_pole(cilova_pozice):
    x_cil, y_cil = cilova_pozice[0], cilova_pozice[1]

    if x_cil >= 1 and x_cil <= 8:
        if y_cil >= 1 and y_cil <= 8:
                return True

def je_pozice_volna(cilova_pozice, obsazena):
    if cilova_pozice in tuple(obsazena):
        return False
    return True

def je_mozny_pohyb(typ_figurky, momentalni_pozice, cilova_pozice, obsazena_pole):
    x_start, y_start = momentalni_pozice[0], momentalni_pozice[1]
    x_cil, y_cil = cilova_pozice[0], cilova_pozice[1]

    if je_pozice_volna(cilova_pozice, obsazena_pole):
        match typ_figurky:

            case "pěšec":
                # Pěšec se může pohnout o dvě pole dopředu z výchozí pozice
                if x_start == 2 and x_cil == x_start + 2 and y_cil == y_start:
                    return True
                # Pěšec se může pohnout o jedno pole dopředu
                if x_cil == x_start + 1 and y_cil == y_start:
                    return True
            
            case "jezdec":
                # Jezdec se může pohnout ve tvaru "L"
                if (abs(x_cil - x_start) == 2 and abs(y_cil - y_start) == 1) or \
                (abs(x_cil - x_start) == 1 and abs(y_cil - y_start) == 2):
                    return True
            
            case "věž":
                if x_cil == x_start:  # Vertikální pohyb
                    for y in range(min(y_start, y_cil) + 1, max(y_start, y_cil)):
                        if (x_start, y) in obsazena_pole:
                            return False
                    return True
                elif y_cil == y_start:  # Horizontální pohyb
                    for x in range(min(x_start, x_cil) + 1, max(x_start, x_cil)):
                        if (x, y_start) in obsazena_pole:
                            return False
                return True

            case "střelec":
                if abs(x_cil - x_start) == abs(y_cil - y_start):  # Diagonální pohyb
                    step_x = 1 if x_cil > x_start else -1
                    step_y = 1 if y_cil > y_start else -1
                    x, y = x_start + step_x, y_start + step_y
                    while (x, y) != (x_cil, y_cil):
                        if (x, y) in obsazena_pole:
                            return False
                        x += step_x
                        y += step_y
                    return True
            
            case "dáma":
                 # Dáma kombinuje pohyby věže a střelce
                if je_tah_mozny(vez, cilova_pozice, obsazena_pole) or je_tah_mozny(strelec, cilova_pozice, obsazena_pole):
                    return True
            
            case "král":
                if abs(x_cil - x_start) <= 1 and abs(y_cil - y_start) <= 1:
                    return True

    return False

def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice): #Ověří, zda se figurka může přesunout na danou pozici.
    """
    #1.ověřte, jestli cilova_pozice neni mimo šachovnic                                     #DONE
    #2.ověřte, zda je daná pozice volná                                                     #DONE
    #3.ověřte, zda je pro danou figuru tato pozice přípustná (vzhledem k pohybu figur)      #DONE
    #4.ověřte, zda v cestě k dané pozici nestojí jiná figura                                #DONE
    
    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    :return: True, pokud je tah možný, jinak False.
    """
    if overeni_mimo_hraci_pole(cilova_pozice) and je_pozice_volna(cilova_pozice, obsazene_pozice) \
        and je_mozny_pohyb(figurka["typ"], figurka["pozice"], cilova_pozice, obsazene_pozice) and \
            cesta_volna(figurka["pozice"], cilova_pozice, obsazene_pozice):
        return True
    return False

if __name__ == "__main__":

    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # True, při prvním tahu, může pěšec jít o 2 pole dopředu
    print(je_tah_mozny(pesec, (5, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o tři pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat
    print()
    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici
    print()
    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True
    print()
    print(je_tah_mozny(strelec, (1, 8), obsazene_pozice))  # True