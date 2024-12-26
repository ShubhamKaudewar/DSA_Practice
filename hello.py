def main():
    from more_itertools import distinct_permutations as idp
    for p in idp(["word","good","best","word"]):
        print(p)


if __name__ == "__main__":
    main()
