class Solution(object):
    def intToRoman(self, number):
        """
        :type num: int
        :rtype: str
        """

        # main conversion table
        conversion = [
            [1, "I"],
            [5, "V"],
            [10, "X"],
            [50, "L"],
            [100, "C"],
            [500, "D"],
            [1000, "M"],
            [5000, "t"]
        ]

        # subtractive symbols
        subtractive = {
            100: ("C", "D", "M"),  # 400 = CD, 900 = CM
            10: ("X", "L", "C"),   # 40 = XL, 90 = XC
            1: ("I", "V", "X"),    # 4 = IV, 9 = IX
        }

        # nested helper function
        def convertDec(x, index):
            if x == 0:
                return ""

            # determine place value
            if index == 0:
                place = 1000
            elif index == 1:
                place = 100
            elif index == 2:
                place = 10
            else:
                place = 1

            # subtractive form
            if place in subtractive:
                one, five, ten = subtractive[place]

                if x == 4:
                    return one + five
                elif x == 9:
                    return one + ten

            # additive form
            value = x * place
            s = ""
            c = 0

            while value > 0:
                if c >= len(conversion):
                    break

                if conversion[c][0] > value:
                    value -= conversion[c-1][0]
                    s += conversion[c-1][1]
                    c = 0
                else:
                    c += 1

            return s

        # Build final Roman numeral
        s = ""
        digits = str(number)
        length = len(digits)

        for count, digit in enumerate(digits):
            index = count + (4 - length)
            s += convertDec(int(digit), index)

        return s
