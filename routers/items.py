from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder

from model.items import Item

# instância da rota de itens
router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)

# Dados mocados
items = ["test1", "test2", "test3"]


# Ler todos os itens
@router.get("/")
async def read_items():
    return {"message": jsonable_encoder(items)}


# Ler um item pelo id
@router.get("/{item_id}")
async def read_item(item_id: int):
    try:
        return {"message": items[item_id]}
    except IndexError:
        raise HTTPException(status_code=404, detail="Item not found")


# Adicionar um item
@router.post("/")
async def add_item(item: Item):
    items.append(item.name)
    return {"message": "The item was successfully added!"}


# Deletar item pelo id
@router.delete("/{item_id}")
async def delete_item(item_id: int):
    try:
        del items[item_id]
        return {"message": "The item was successfully removed!"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Item not found")
