from fastapi import APIRouter

router = APIRouter(prefix='/pallindrome', tags=['Pallindrome Numbers'])

def isPallindrome(value: int):
    temp = value
    sum: int = 0

    while value>0:
        digit = value%10
        sum = sum*10 + digit 
        value = value//10
    
    if(temp == sum):
        return True
    else:
        return False


@router.get('/{value}')
def main(value: int):
    return isPallindrome(value)

@router.get('/limit/')
def limit(u: int, l: int):
    data = {}
    for num in range(u,l):
        data[int(num)] = isPallindrome(num)
    return data