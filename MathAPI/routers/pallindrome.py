from fastapi import APIRouter

router = APIRouter(prefix='/pallindrome', tags=['Pallindrome Numbers'])

@router.get('/')
def main():
    return {'detail': 'well done boy'}