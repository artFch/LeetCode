class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        l = len(flowerbed)
        if l == 1 and n == 1 and flowerbed[0] != 1:
            return True
        for i in range(l - 1):
            if flowerbed[i] == 0:
                if i == 0 and flowerbed[i+1] != 1:
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True
                elif flowerbed[i-1] != 1 and flowerbed[i+1] != 1:
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True

                elif flowerbed[-1] == 0 and flowerbed[-2] != 1:
                    flowerbed[-1] = 1
                    n -= 1
                    if n == 0:
                        return True
        print(flowerbed)
        return n == 0
