class Solution(object):
    def isValid(self, s):
        stack = []

        for bracket in s:

            if bracket == "(" or bracket == "[" or bracket == "{":
                stack.append(bracket)

            else:
                if len(stack) == 0:
                    return False

                ch = stack.pop()

                if bracket == ")" and ch == "(":
                    continue

                if bracket == "]" and ch == "[":
                    continue

                if bracket == "}" and ch == "{":
                    continue

                return False

        return len(stack) == 0