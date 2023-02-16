import json
from .OrderMangementException import OrderManagementException
from .OrderRequest import OrderRequest


class OrderManager:
    def __init__(self):
        pass

    def ValidateEAN13( self, eAn13 ):
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

    def ReadproductcodefromJSON( self, fi ):

        try:
            with open(fi) as f:
                DATA = json.load(f)
        except FileNotFoundError as e:
            raise OrderManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from e


        try:
            PRODUCT = DATA["id"]
            PH = DATA["phoneNumber"]
            req = OrderRequest(PRODUCT, PH)
        except KeyError as e:
            raise OrderManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.ValidateEAN13(PRODUCT):
            raise OrderManagementException("Invalid PRODUCT code")

        # Close the file
        return req