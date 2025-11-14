from functools import lru_cache
from typing import Union

from fastapi import FastAPI, Depends
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware

from routers import todos
import config

app = FastAPI()

# ===== CORS =====
# De momento abrimos a todos los orígenes para que no moleste en el bootcamp.
# Cuando quieras puedes limitarlo a tu dominio de Vercel.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://todo-app2-r35e5gxjc-alvarodimoni-9967s-projects.vercel.app" ,
                   "https://todo-app2-66k6.onrender.com" ,
                   "https://todo-app2-teal.vercel.app",
                   "http://localhost:3000",
                   "http://localhost:8000"],          # si quieres, luego lo cambias por una lista concreta
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar las rutas de /todos
app.include_router(todos.router)


# ===== Manejador global de errores HTTP =====
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    print(f"{repr(exc)}")
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


# ===== Configuración =====
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
