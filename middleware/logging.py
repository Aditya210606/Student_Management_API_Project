from fastapi import Request
import time

async def log_request(request:Request, call_next):

    start_time = time.time()

    response = await call_next(request)

    end_time = time.time()

    request_time = end_time - start_time

    print(f'Time taken : {request_time}')

    return response