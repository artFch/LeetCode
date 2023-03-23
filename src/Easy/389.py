class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_list = list(s)
        t_list = list(t)
        s_list.sort()
        t_list.sort()
        print(t_list)
        print(s_list)
        for i in range(len(s_list)):
            if s_list[i] != t_list[i]:
                return t_list[i]
        return t_list[-1]
