def userInputLimit():
    #\/\/\ user limitations \/\/\
    num = int(input("Zadej číslo od 0 do 100: "))
    if (num) < 0 or (num) > 100:
        while (num) < 0 or (num) > 100:
            num = input("Špatně zadané číslo. Zadej znovu číslo od 0 do 100: ")
        return (num)
    else:
        return (num)

def cislo_text (cislo):
    # funkce, která zkonvertuje číslo do náležité textové reprezentace.
    numDict = {
        0: "nula",
        1: "jedna",
        2: "dva",
        3: "tři",
        4: "čtyři",
        5: "pět",
        6: "šest",
        7: "sedm",
        8: "osm",
        9: "devět",
        10: "deset",
        20: "dvacet",
        30: "třicet",
        40: "čtyřicet",
        50: "padesát",
        60: "šedesát",
        70: "sedmdesát",
        80: "osmdesát",
        90: "devadesát",
        100: "sto"
    }
    match cislo:
        case 11:
            return "jedenáct"
        case 14:
            return "čtrnáct"
        case 15:
            return "patnáct"
        case 19:
            return "devatenáct"
        case 100:
            return numDict[cislo]

    if cislo > 11 and cislo < 20:
        lt = str(cislo/10).split(".",2)
        jednotky = int(lt[1])
        return numDict[jednotky] + "náct"
    elif (cislo) > 20 and cislo not in numDict:
        lt = str(cislo/10).split(".",2)
        desitky = int(lt[0]) * 10
        jednotky = lt[1]
        return numDict[desitky] + " " + numDict[int(jednotky)]
    else:
        return numDict[int(cislo)]
    
if __name__ == "__main__":
    cislo = userInputLimit()
    text = cislo_text(cislo)
    print(text)