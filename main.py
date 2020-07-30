import uvicorn
from fastapi import FastAPI

# from test.base_route import GzipRoute
from apps.host.view import router as h_router
from apps.white_list.view import router as w_router
from apps.attack_log_whitelist.view import router as a_w_router
from apps.attack_log.view import router as a_router

app = FastAPI()
app.include_router(h_router, prefix="/api")
app.include_router(w_router, prefix="/api")
app.include_router(a_w_router)
app.include_router(a_router)


# app.router.route_class = GzipRoute

@app.get("/")
async def root():
    # TODO:返回index.html
    return {"message": "Hello World"}


if __name__ == '__main__':
    uvicorn.run(app='main:app', host="127.0.0.1", port=8000, reload=True, debug=True)
