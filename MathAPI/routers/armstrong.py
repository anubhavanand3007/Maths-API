from typing import Optional
from fastapi import APIRouter

router = APIRouter(prefix='/armstrong', tags=['Armstrong Numbers'])

def isArmstrong(value: int):
    temp = value
    sum: int = 0

    while value>0:
        digit = value%10
        sum += digit**3 
        value = value//10
    
    if(temp == sum):
        return True
    else:
        return False


@router.get('/{value}')
def main(value: int):
    return isArmstrong(value)

@router.get('/limit')
def limit(u: int, l: int):
    data = {}
    for num in range(u,l):
        data[int(num)] = isArmstrong(num)
    return data