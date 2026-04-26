#uvicorn app:app --reload    le moteur qui execute ton code et repondd au requetes de http

from fastapi import FastAPI,Request #creation de lapi
from routes.fruits import router as fruits_router #import de tout mon routes de fruit
from routes.crews import router as crews_router 

from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
app = FastAPI()#creat app
app.mount("/templates", StaticFiles(directory="templates"), name="templates")

@app.get("/")
def root():
    return FileResponse("templates/index.html")


app.include_router(fruits_router, prefix="/fruits")#!important ca connecte tout a mon app 
#le prefix fruit et pour tout les url

app.include_router(crews_router, prefix="/crews")#!important ca connecte tout a mon app 