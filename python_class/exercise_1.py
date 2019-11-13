#Write a Python program to convert an integer to a roman numeral.

class Numbers:
    def int_to_roman(self, number_i):
        value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_numbers = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        roman_num = []
        for i in range(len(value)):
            count = int(number_i / value[i])
            roman_num.append(roman_num[i]*count)
            number_i = number_i - count
        return ''.join(roman_num)
