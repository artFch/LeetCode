class Solution:
    def interpret(self, command: str) -> str:
        result = ""
        for i in range(len(command)):
            if command[i] == "G":
                result += "G"
            if command[i] == "(":
                j = i
            if command[i] == ")":
                if i - j == 1:
                    result += "o"
                else:
                    result += "al"
        return result
