from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
from json import dumps
from fastapi.staticfiles import StaticFiles

class App(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        @self.get("/api")
        async def root(request: Request):
            return JSONResponse(content=dumps(dict(request.headers)))

        @self.get("/")
        async def root(request: Request):
            return HTMLResponse(open("www/index.html").read())
        
        self.mount("/", StaticFiles(directory="www", html=True), name="www")