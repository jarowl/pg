def userInputLimit(cislo):
    #\/\/\ user limitations \/\/\
    num_input = cislo
    num = int(num_input)
    if (num) < 0 or (num) > 100:
        return None
    else:
        return (num)

def cislo_text (cislo):
    # funkce, která zkonvertuje číslo do náležité textové reprezentace.
    num = userInputLimit(cislo)
    if num != None :
        num = int(cislo)
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
        match num:
            case 11:
                return "jedenáct"
            case 14:
                return "čtrnáct"
            case 15:
                return "patnáct"
            case 19:
                return "devatenáct"
            case 100:
                return numDict[num]

        if num > 11 and num < 20:
            lt = str(num/10).split(".",2)
            jednotky = int(lt[1])
            return numDict[jednotky] + "náct"
        elif (num) > 20 and num not in numDict:
            lt = str(num/10).split(".",2)
            desitky = int(lt[0]) * 10
            jednotky = lt[1]
            return numDict[desitky] + " " + numDict[int(jednotky)]
        else:
            return numDict[int(num)]
    
    return None
    
if __name__ == "__main__":
    text = cislo_text("112")
    print(text)