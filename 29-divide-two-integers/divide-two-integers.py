class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        count = 0

        if dividend >= 0 and divisor >= 0:
            posi = True

        elif dividend < 0 and divisor < 0:
            dividend = -dividend
            divisor = -divisor
            posi = True

        else:
            if dividend < 0:
                dividend = -dividend
                posi = False
            else:
                divisor = -divisor
                posi = False

        while dividend >= divisor:
            current_divisor = divisor
            current_count = 1

            while dividend >= current_divisor + current_divisor:
                current_divisor += current_divisor
                current_count += current_count

            dividend -= current_divisor
            count += current_count

        if posi:
            return min(count, 2**31 - 1)
        else:
            return -count