from fastapi import FastAPI
app=FastAPI()
@app.get("/sqrt/{n}")
def sqrt(n:int):
    return{"input":n ,"square":n*n}