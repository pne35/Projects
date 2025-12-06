class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < -2147483648 or x > 2147483648:
            return 0
        elif x < 0:
            v = int("-" + str(x)[::-1][:-1])
            if v < -2147483648:
                return 0
            return v
        else:
            v = int(str(x)[::-1])
            if v > 2147483648:
                return 0
            return v
