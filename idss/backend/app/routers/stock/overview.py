from fastapi import APIRouter

router = APIRouter()


@router.get('/')
def get_overview_list():
    pass


@router.get('/<code>')
def get_overview(code):
    pass


@router.post('/<code>')
def post_overview(code):
    pass
