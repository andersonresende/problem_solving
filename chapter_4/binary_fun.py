
class DecimalConverter(object):
    def __init__(self, number):
        self.number = number

    def convert(self, base):
        """
        Convert a decimal number in self.number attribute to base required,
        :param base: int
        :return: list
        """
        number = self.number
        converted_number = []
        while number:
            rest = number % base
            converted_number.append(rest)
            number = number / base
        return converted_number[::-1]

    def format_hex(self, list_converted):
        """
        Format chars hexadecimal numbers,
        :param list_converted: list
        :return: list
        """
        dict_hex = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        list_converted = [dict_hex[n] if n in dict_hex.keys() else str(n) for n in list_converted]
        return list_converted

    def to_bin(self):
        list_converted = [str(n) for n in self.convert(2)]
        return ''.join(list_converted)

    def to_octal(self):
        list_converted = [str(n) for n in self.convert(8)]
        return ''.join(list_converted)

    def to_hex(self):
        list_converted = self.format_hex(self.convert(16))
        return ''.join(list_converted)


print DecimalConverter(200).to_bin()
print DecimalConverter(200).to_octal()
print DecimalConverter(256).to_hex()


class DecimalConvertExpert(object):
    def __init__(self, number):
        self.number = number

    def baseConverter(self,base):
        digits = '0123456789ABCDEF'
        decNumber = self.number
        list_converted = []
        while decNumber > 0:
            rem = decNumber % base
            list_converted.append(rem)
            decNumber = decNumber / base
        newString = ""
        while len(list_converted):
            newString += digits[list_converted.pop()]
            list_converted = list_converted[:len(list_converted)]
        return newString

    def to_bin(self):
        return self.baseConverter(2)
    def to_oct(self):
        return self.baseConverter(8)
    def to_hex(self):
        return self.baseConverter(16)

print DecimalConvertExpert(200).baseConverter(16)

def cbd(n):
    """
    Converte de binario para decimal usando reduce e compression.
    :param n: int
    :return: int
    """
    return reduce(lambda a,b: a+b, \
           [int(n) * (2 ** int(i)) for n,i in enumerate(str(n)[::-1])])

print map(cbd, [10,1010])