def overeni_mimo_hraci_pole(cilova_pozice):
    if cilova_pozice[0] >= 1 and cilova_pozice[0] <= 8:
        if cilova_pozice[1] >= 1 and cilova_pozice[1] <= 8:
                return True
def je_pozice_volna(cilova_pozice, obsazena):
    if cilova_pozice in tuple(obsazena):
        return False
    return True
def je_mozny_pohyb(typ_figurky, momentalni_pozice, cilova_pozice, obsazena):
    if je_pozice_volna(cilova_pozice, obsazena):
        match typ_figurky:
            case "pěšec":
                if  momentalni_pozice[1] == 1 and momentalni_pozice[1] + 2 == cilova_pozice[1]:
                    return True
                elif momentalni_pozice[1] + 1 == cilova_pozice[1]:
                    return True
            case "jezdec":
                pozice1 = momentalni_pozice[0] + 1 and momentalni_pozice[1] + 2
                pozice2 = momentalni_pozice[0] + 2 and momentalni_pozice[1] + 1
                pozice3 = momentalni_pozice[0] + 2 and momentalni_pozice[1] - 1
                pozice4 = momentalni_pozice[0] + 1 and momentalni_pozice[1] - 2
                pozice5 = momentalni_pozice[0] - 1 and momentalni_pozice[1] - 2
                pozice6 = momentalni_pozice[0] - 2 and momentalni_pozice[1] - 1
                pozice7 = momentalni_pozice[0] - 2 and momentalni_pozice[1] + 1
                pozice8 = momentalni_pozice[0] - 1 and momentalni_pozice[1] + 2
                
                if pozice1 == cilova_pozice or pozice2 == cilova_pozice or pozice3 == cilova_pozice or pozice4 == cilova_pozice or pozice5 == cilova_pozice or pozice6 == cilova_pozice or pozice7 == cilova_pozice or pozice8 == cilova_pozice:
                    return True
            case "věž":
                if momentalni_pozice[0] == cilova_pozice[0]:  # Horizontálně
                    for y in range(min(momentalni_pozice[1], cilova_pozice[1]) + 1, max(momentalni_pozice[1], cilova_pozice[1])):
                        if (momentalni_pozice[0], y) in obsazena:
                            return False
                    return True
                        
                elif momentalni_pozice[1] == cilova_pozice[1]:  # Vertikálně
                    for x in range(min(momentalni_pozice[0], cilova_pozice[0]) + 1, max(momentalni_pozice[0], cilova_pozice[0])):
                        if (x, momentalni_pozice[1]) in obsazena:
                            return False
                    return True
            case "střelec":
                pass
            case "dáma":
                pass
            case "král":
                pass

    return False

def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice): #Ověří, zda se figurka může přesunout na danou pozici.

    """
    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """
    if overeni_mimo_hraci_pole(cilova_pozice) and je_pozice_volna(cilova_pozice, obsazene_pozice) and je_mozny_pohyb(figurka["typ"], figurka["pozice"], cilova_pozice, obsazene_pozice):
        return True
    

    #1.ověřte, jestli cilova_pozice neni mimo šachovnic                                     #DONE
    #2.ověřte, zda je daná pozice volná                                                     #DONE
    #3.ověřte, zda je pro danou figuru tato pozice přípustná (vzhledem k pohybu figur)      #TODO
    #4.ověřte, zda v cestě k dané pozici nestojí jiná figura                                #TODO
    return False


if __name__ == "__main__":

    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    #print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici
    #print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    #print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    #print("")
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat
    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)    

"""
    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o dvě pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True
"""