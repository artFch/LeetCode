def difference(n):
    mult = 1
    summ = 0
    while n > 0:
        last = n % 10
        mult *= last
        summ += last
        n = n // 10

    return mult - summ


def main():
    n = 4421
    print(difference(n))


main()
