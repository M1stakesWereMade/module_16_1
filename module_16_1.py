from fastapi import FastAPI
from pydantic import BaseModel

# Создаем объект FastAPI
app = FastAPI()

# Маршрут главной страницы
@app.get("/")
def read_main():
    return {"message": "Главная страница"}

# Маршрут страницы администратора
@app.get("/user/admin")
def read_admin():
    return {"message": "Вы вошли как администратор"}

# Маршрут страницы пользователя с параметром в пути
@app.get("/user/{user_id}")
def read_user(user_id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

# Маршрут страницы пользователя с параметрами в адресной строке
class UserInfo(BaseModel):
    username: str
    age: int

@app.get("/user")
def read_user_info(user_info: UserInfo):
    return {
        "message": f"Информация о пользователе. Имя: {user_info.username}, Возраст: {user_info.age}"
    }
