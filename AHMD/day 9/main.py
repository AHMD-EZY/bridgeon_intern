from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
class LoginData(BaseModel):
    email:str
    password:str
@app.post("/login")
def login(data:LoginData):
    if data.email=="ahmd@gmail.com" and data.password=="ayas123":
        return{"message":"login success",
               "token":"abc123"}    
    raise HTTPException(status_code=401, detail="invalid email or password")
