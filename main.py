from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware

from routers.items import router as router_item

# Instãncia da API
app = FastAPI(title="MyAPI",
              description="Welcome to my test API, enjoy!",
              contact={
                  "name": "Audrey Teles",
                  "email": "audreytelesdossantos@gmail.com",
              },
              )
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Adiciona a rota de item na api
app.include_router(router_item)

if __name__ == '__main__':
    uvicorn.run(app, port=8080)
