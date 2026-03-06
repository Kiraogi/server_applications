# from fastapi_swagger_ui import SwaggerUI
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional

import logging
from routes.users import router as user_router

class User(BaseModel):
    name: str = Field(..., example="Jon")
    age: int = Field(..., example=25)
    email: str = Field(..., example="jon@gmail.com")

class UpdateUser(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None

# Настройки логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="API Сервис",
    description="Документация API с примерами и подробным описанием",
    version="1.0.0",
    contact={
        "name": "Разработчик",
        "email": "Dev@mail.ru",
        "url": "https://example.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT"
    },
    # openapi_url="/api/openapi.json",
    # docs_url="/api/docs",
    # redoc_url=None,
)

# app.mount("/swagger",
#           SwaggerUI(app, swagger_ui_parameters={"defaultModelExpandDepth": -1}))


app.include_router(user_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Разрешить все источники
    allow_credentials=True,
    allow_methods=["*"], # Разрешить все методы (GET, POST, PUT, DELETE)
    allow_headers=["*"], # Разрешить все заголовки
)

@app.get("/")
def home():
    logger.info("Обработан запрос к корневому маршруту")
    return {
        "status": "ok",
        "message": "Welcome to FastAPI Training"
    }

@app.post("/users")
def create_user(user: User):
    return {"message": f'Пользователь {user.name} создан!', "data": user}

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    return {"user_id": user_id, "updated_data": user}

@app.patch("/users/{user_id}")
def update_partial_user(user_id: int, user: UpdateUser):
    return {"user_id": user_id, "update_fields": user.dict(exclude_none=True)}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return {"message": f'Пользователь с ID {user_id} удален!'}

@app.get("/users/{user_id}", 
         summary="Получение информации о пользователе",
         description="Возвращает данные пользователя по его ID."
         )
def get_user(user_id: int):
    return {"user_id": user_id, "name": "John Doe", "email": "johndoe@example.com"}

@app.post("/users/", summary="Создание пользователя")
def create_user(user: User):
    """Добавляет нового пользователя в систему"""
    return {"message": f'Пользователь создан.', "user": user}

@app.get(
    "/users/{user_id}",
    response_model=User,
    responses={404: {"description": "Пользователь не найдет"}}
)
def get_user(user_id: int):
    if user_id != 1:
        raise HTTPException(status_code=404, detail="Пользователь не найдет")
    return {"name": "Иван", "age": 50, "email": "ivan@example.com"}

@app.get("/users/{user_id}", tags=["Пользователи"])
def get_user(user_id: int):
    return {"user_id": user_id}

@app.get("/orders/{order_id}", tags=["Заказы"])
def get_order(order_id:int):
    return {"order_id": order_id, "status": "Оплачено!"}

@app.get("/debug")
def debug_route():
    x = 10
    y = 20
    breakpoint() # Остановка выполнения здесь
    return {"result": x + y}