from fastapi import FastAPI, HTTPException, Path,Depends
from fastapi.responses import JSONResponse
from models import Student,UpdateStudent,StudentResponse,StudentSearch
from data import load_data, save_data
from routers.student import router
from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from exceptions.handlers import http_exception_handler,request_validatorError_handler,generic_exception_handler
from middleware.logging import log_request
import time

app =FastAPI()

# includes all the routes from the router file in the app 
app.include_router(router)

# this are the methods to register the expections   
app.add_exception_handler( HTTPException, http_exception_handler)

app.add_exception_handler(RequestValidationError,request_validatorError_handler)

app.add_exception_handler(Exception, generic_exception_handler)

app.middleware('http')(log_request)













    


