class RomanNumerals:
    ROM = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }
    @staticmethod
    def to_roman(val : int) -> str:
        result = ''

        for numeral, value in RomanNumerals.ROM.items():
            count = val // value
            if count > 0:
                result += numeral * count
                val -= value * count
        return result

    @staticmethod
    def from_roman(roman_num : str) -> int:  
        num = 0
        for numeral, value in RomanNumerals.ROM.items():
            while roman_num.startswith(numeral):
                num += value
                roman_num = roman_num[len(numeral):]
        return num