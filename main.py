from fastapi import FastAPI, HTTPException, Path,Depends
from fastapi.responses import JSONResponse
from models import Student,UpdateStudent,StudentResponse,StudentSearch
from data import load_data, save_data
from routers.student import router


app = FastAPI()
app.include_router(router)
  


# this endpoint is to delete the existing student in the json data








    


