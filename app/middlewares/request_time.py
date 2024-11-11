import time
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

class RequestTimeMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        response: Response = await call_next(request)
        
        process_time = time.time() - start_time
        
        print(f"Request to {request.url} took {process_time:.4f} seconds")
        
        return response
