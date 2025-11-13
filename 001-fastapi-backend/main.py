from functools import lru_cache
from typing import Union

from fastapi import FastAPI, Depends
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException

from routers import todos
import config

app = FastAPI()

# ========= CORS =========
# De momento dejamos todo abierto. Más tarde se puede limitar a tu dominio de Vercel.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # aquí luego podrías poner tu dominio de Vercel si quieres
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ========= Routers =========
app.include_router(todos.router)

# ========= Handlers =========
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    print(repr(exc))
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

# ========= Settings =========
@lru_cache()
def get_settings():
    return config.Settings()

@app.get("/")
def read_root(settings: config.Settings = Depends(get_settings)):
    print(settings.app_name)
    return "Hello World"

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
