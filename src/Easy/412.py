class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        a = list(range(1, n+1))
        for i in range(len(a)):
            if a[i] % 15 == 0:
                a[i] = "FizzBuzz"
            elif a[i] % 5 == 0:
                a[i] = "Buzz"
            elif a[i] % 3 == 0:
                a[i] = "Fizz"
            else:
                a[i] = str(a[i])
        return a
