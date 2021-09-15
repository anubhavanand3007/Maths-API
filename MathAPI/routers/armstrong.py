from fastapi import APIRouter

router = APIRouter(prefix='/armstrong', tags=['Armstrong Numbers'])

@router.get('/')
def main():
    return {'detail': 'well done boy'}