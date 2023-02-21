""""
Módulo Order Manager. Encargado de leer y validar el codigo recibido.
"""

import json
from .order_mangement_exception import ORDERMANAGEMENTEXCEPTION
from .order_request import ORDERREQUEST


class ORDERMANAGER:
    """
    Clase ORDERMANAGER.
    """
    def __init__(self):
        """
        Funcion constructora de la clase ORDERMANAGER
        """
        pass

    def validateEAN13(self, eAn13):
        """

        :param eAn13:
        :return: True o False si el codigo es del tipo EAN13
        """
        # PLEASE INCLUDE HERE THE CODE FOR VALIDATING THE GUID
        # RETURN TRUE IF THE GUID IS RIGHT, OR FALSE IN OTHER CASE
        if len(eAn13) != 13:
            return False
        impares = 0
        pares = 0
        for i in range(len(eAn13)-1):
            if i % 2 == 0:
                impares = impares + int(eAn13[i])
            else:
                pares = pares + int(eAn13[i])
        impares = impares*3
        total = impares+pares
        dec = total // 10
        dec = (dec + 1) * 10
        digito_control = dec - total
        if digito_control % 10 == 0:
            digito_control = 0
        if int(eAn13[12]) != digito_control:
            return False
        return True

    def readProductCodeFromJson(self, varFi):
        """

        :param varFi:
        :return: Nada. Lee y si hay error lanza una excepción
        """
        try:
            with open(varFi) as var_f:
                data = json.load(var_f)
        except FileNotFoundError as var_e:
            raise ORDERMANAGEMENTEXCEPTION("Wrong file or file path") from var_e
        except json.JSONDecodeError as var_e:
            raise ORDERMANAGEMENTEXCEPTION("JSON Decode Error - Wrong JSON Format") from var_e


        try:
            product = data["id"]
            var_ph = data["phoneNumber"]
            req = ORDERREQUEST(product, var_ph)
        except KeyError as var_e:
            raise ORDERMANAGEMENTEXCEPTION("JSON Decode Error - Invalid JSON Key") from var_e
        if not self.validateEAN13(product):
            raise ORDERMANAGEMENTEXCEPTION("Invalid PRODUCT code")

        # Close the file
        return req
