from fastapi import FastAPI, HTTPException, Path,Depends
from fastapi.responses import JSONResponse
from models import Student,UpdateStudent,StudentResponse,StudentSearch
from data import load_data, save_data
from routers.student import router
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from exceptions.handlers import http_exception_handler,request_validatorError_handler

app =FastAPI()

app.include_router(router)
  


app.add_exception_handler( HTTPException, http_exception_handler)

app.add_exception_handler(RequestValidationError,request_validatorError_handler)










    


