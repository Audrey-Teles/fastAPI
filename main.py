from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
import uvicorn

app = FastAPI(title="MyPortfolio",
              description="Welcome to my portfolio, here all my programming"
                          "skills can be manipulated as in an API, enjoy!",
              contact={
                  "name": "Audrey Teles",
                  "email": "audreytelesdossantos@gmail.com",
              },
              )

lista = []


@app.get("/", tags=["Welcome"])
async def root():
    return {"message": "Welcome to my API for tests!"}


@app.post("/item/{name}", tags=["Items"])
async def add_item(name: str):
    lista.append(name)
    return {"message": "The item was successfully added!"}


@app.get("/allitems", tags=["Items"])
async def all_items():
    return {"message": jsonable_encoder(lista)}


@app.delete("/item/{name}", tags=["Items"])
async def delete_item(name: str):
    lista.remove(name)
    return {"message": "The item was successfully removed!"}


if __name__ == '__main__':
    uvicorn.run(app, port=8080)
