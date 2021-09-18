from fastapi import APIRouter
from typing import NewType, Optional

router = APIRouter(prefix='/NumberSystem', tags=['Number System'])

class Decimal:
    value = 0

    def __init__(self,value):
        self.value = value

    def toBinary(self):
        temp = self.value
        sum =0
        i =1
        while(temp > 0):
            digit = temp%2
            sum += digit*(10**i)
            temp = temp//2
            i+=1
        return sum

    def toOct(self):
        temp = self.value
        sum =0
        i =1
        while(temp > 0):
            digit = temp%8
            sum += digit*(10**i)
            temp = temp//8
            i+=1
        return sum

    def toHexa(self):
        temp = self.value
        sum = []
        i =1
        while(temp > 0):
            digit: str = temp%16
            if(digit>=0 and digit<=9):  
                sum.insert(0, str(digit))
            else:
                sum.insert(0, chr(ord('A')+digit-10))
            temp = temp//16
            i+=1

        data = "".join(sum)  
        return data

@router.get("/decimalto")
def binaryto(value: int, binary: Optional[bool] = None, oct: Optional[bool] = None,hexa: Optional[bool] = None):
    item = {
        'decimal': value
    }
    
    a = Decimal(value)

    if binary:
        item['binary']= a.toBinary()
    if oct:
        item['ocatal'] = a.toOct()
    if hexa:
        item['hexadecimal'] = a.toHexa()
    
    return item