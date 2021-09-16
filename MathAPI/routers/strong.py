from typing import Optional
from fastapi import APIRouter

router = APIRouter(prefix='/strong', tags=['Strong Numbers'])

def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i
    return fact

def isStrong(value: int):
    temp = value
    sum: int = 0

    while value>0:
        digit = value%10
        sum += factorial(digit) 
        value = value//10
    
    if(temp == sum):
        return True
    else:
        return False


@router.get('/{value}')
def main(value: int):
    return isStrong(value)

@router.get('/limit')
def limit(u: int, l: int):
    data = {}
    for num in range(u,l):
        data[int(num)] = isStrong(num)
    return data