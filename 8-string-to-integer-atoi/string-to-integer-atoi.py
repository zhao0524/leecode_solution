class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        state = 1
        started = False

        for i in s:
            if i == " " and not started:
                continue

            elif i == "-" and not started:
                state = -1
                started = True

            elif i == "+" and not started:
                started = True

            elif i.isdigit():
                started = True

                if result * 10 + int(i) > 2**31 - 1:
                    if state == 1:
                        return 2**31 - 1
                    else:
                        return -2**31

                result = result * 10 + int(i)

            else:
                break

        return result * state