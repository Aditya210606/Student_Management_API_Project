from fastapi import FastAPI, HTTPException, Path,Depends
from fastapi.responses import JSONResponse
from schemas.students import Student,UpdateStudent,StudentResponse,StudentSearch
from data import load_data, save_data
from routers.student import router as studentrouter
from routers.teacher import router as teacherrouter
from routers.department import router as departmentrouter
from routers.subject import router as subjectrouter
from routers.attendance import router as attendancerouter
from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from exceptions.handlers import http_exception_handler,request_validatorError_handler,generic_exception_handler
from middleware.logging import log_request
from core.config import settings
from fastapi.middleware.cors import CORSMiddleware
import time
from database.connection import engine
from database.base import Base
from database.database import *

#settings
app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# this are the methods to register the expections   
app.add_exception_handler( HTTPException, http_exception_handler)

app.add_exception_handler(RequestValidationError,request_validatorError_handler)

app.add_exception_handler(Exception, generic_exception_handler)

app.middleware('http')(log_request)


# includes all the routes from the router file in the app 
app.include_router(studentrouter)
app.include_router(teacherrouter)
app.include_router(departmentrouter)
app.include_router(subjectrouter)
app.include_router(attendancerouter)
#This creates all the table in the database
Base.metadata.create_all(bind=engine)











    


