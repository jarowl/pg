def my_range(start, stop, step=1):
    i = start
    results = []
    while i < stop:
        results.append(i)
        i += step
    return results


    

if __name__ == "__main__":
    seznam = list(range(1, 10))
    print (seznam)

    seznam = my_range(1, 10)
    print(seznam)