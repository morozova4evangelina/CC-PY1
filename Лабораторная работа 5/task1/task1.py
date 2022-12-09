from pprint import pprint


def number():
    number_dict = []
    list_ = range(0, 16)

    for num in list_:

        n_bin = bin(num)
        n_dec = int(num)
        n_hex = hex(num)
        n_oct = oct(num)

        number_dict.append({"bin":n_bin, "dec":n_dec, "hex":n_hex, "oct":n_oct})
    return number_dict

pprint(number())
