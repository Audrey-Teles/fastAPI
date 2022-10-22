from fastapi import FastAPI
import uvicorn

from routers.items import router as router_item

# Instãncia da API
app = FastAPI(title="MyAPI",
              description="Welcome to my test API, enjoy!",
              contact={
                  "name": "Audrey Teles",
                  "email": "audreytelesdossantos@gmail.com",
              },
              )

# Adiciona a rota de item na api
app.include_router(router_item)

if __name__ == '__main__':
    uvicorn.run(app, port=8080)
