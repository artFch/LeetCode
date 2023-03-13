def salary_medium(salary):
    summ = 0
    non = max(salary) + min(salary)
    for i in range(0, len(salary)):
        summ += salary[i]
    summ -= non
    return summ/(i-1)


# def main():
#     salary = [4000, 3000, 1000, 2000]
#     print(salary_medium(salary))


# main()
