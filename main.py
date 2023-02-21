"""
modulo de Main
"""
import string
from barcode import EAN13
from barcode.writer import ImageWriter
from uc3m_logistics import ORDER_MANAGER


#GLOBAL VARIABLES
CT_letter = string.ascii_letters + string.punctuation + string.digits
CT_shifts = 3


def Encode(word):
    """
    :param word:
    :return: encoded
    """
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            var_x = (CT_letter.index(letter) + CT_shifts) % len(CT_letter)
            encoded = encoded + CT_letter[var_x]
    return encoded

def Decode(word):
    """
    :param word:
    :return: encoded
    """
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            var_x = (CT_letter.index(letter) - CT_shifts) % len(CT_letter)
            encoded = encoded + CT_letter[var_x]
    return encoded

def Main():
    """
    definición de la funcion Main
    no recibe parametros ni returns
    """
    mng = ORDER_MANAGER()
    res = mng.readProductCodeFromJson("test.json")
    str_res = str(res)
    print(str_res)
    encode_res = Encode(str_res)
    print("Encoded Res " + encode_res)
    decode_res = Decode(encode_res)
    print("Decoded Res: " + decode_res)
    print("Codew: " + res.product_code)
    with open("./barcodeEan13.jpg", 'wb') as var_f:
        var_iw = ImageWriter()
        EAN13(res.product_code, writer=var_iw).write(var_f)


if __name__ == "__main__":
    Main()
