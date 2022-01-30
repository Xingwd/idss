from fastapi import APIRouter
from fds.stock.index import Index

router = APIRouter()
index = Index()

@router.get('/shang_zheng_50')
async def get_shang_zheng_50():
    pass


@router.post('/shang_zheng_50')
async def post_shang_zheng_50():
    df = index.shang_zheng_50
    pass


@router.get('/hu_shen_300')
async def get_hu_shen_300():
    pass


@router.post('/hu_shen_300')
async def post_hu_shen_300():
    df = index.hu_shen_300
    pass
