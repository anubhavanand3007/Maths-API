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


@router.get('/')
def main(value: int):
    return {value: isArmstrong(value)}