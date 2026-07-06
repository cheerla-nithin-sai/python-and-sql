# Last updated: 7/6/2026, 8:48:07 AM
1class Solution:
2    def addStrings(self, num1: str, num2: str) -> str:
3        import sys
4        sys.set_int_max_str_digits(0)
5        return str(int(num1)+int(num2))
6
7        