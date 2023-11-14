def myzip(it1, it2):
    print(f"Zipping {it1} and {it2}")
    iterator1, iterator2 = iter(it1), iter(it2)
    while True:
        try:
            yield next(iterator1), next(iterator2)
        except StopIteration:
            break
    print("Zip completed.")
##tools/numbers/col.py