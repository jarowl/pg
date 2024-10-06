# funkce vypise "Číslo X je sudé" pokud je cislo sude a "Číslo X je liché" pokud je cislo liche
def sudy_nebo_lichy(cislo):
    if cislo%2 == 0:
        print("Cislo", cislo, "je sude")
    else:
        print("Cislo", cislo, "je liche")
#test
sudy_nebo_lichy(5)
sudy_nebo_lichy(1000000)
