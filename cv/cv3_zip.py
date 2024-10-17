def my_zip(*iterables):
    """
    Nase vlastni implementace zip()

        iterables = [
         jmena = ["Alice", "Bob", "Karel", "Eva", "Martin"], -> len() -> 5
         vek =   [     30,    20,      24,    18,      27 ]
         vaha =  [     50,    80,      90,    55,      67 ]
        ]

    result =  [
    
    ]
    """
    results = []
    length = len(iterables[0])
    i = 0

    while (i < length):
        subresult = []
        for iterable in iterables:
            subresult.append(iterable[i])
        results.append(tuple(subresult) )
        i += 1
    return results
if __name__ == "__main__":
    
    jmena = ["Alice", "Bob", "Karel", "Eva", "Martin"]
    vek =   [     30,    20,      24,    18,      27 ]
    vaha =  [     50,    80,      90,    55,      67 ]

    vysledek = list(zip(jmena, vek, vaha))
    print (vysledek)
    #for jmeno, vek, vaha in vysledek:
        #print(f'{jmeno} je {vek} let a vazi {vaha}')

    vylsedek = my_zip(jmena, vek, vaha)
    print (vysledek)