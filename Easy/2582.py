class Solution(object):
    def passThePillow(self, n, time):
        ret = 0
        rounds = (time/(n-1))
        print(rounds)
        i = time % (n-1)
        print(i)
        if (rounds % 2 == 0):
            ret = i+1
            print(ret)
            return ret
        else:
            ret = n - i
            print(ret)
            return ret
