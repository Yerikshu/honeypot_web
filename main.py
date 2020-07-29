import uvicorn
from fastapi import FastAPI

# from test.base_route import GzipRoute
from apps.host.view import router as h_router
from apps.white_list.view import router as w_router

app = FastAPI()
app.include_router(h_router, prefix="/api")
app.include_router(w_router, prefix="/api")


# app.router.route_class = GzipRoute

@app.get("/")
async def root():
    # TODO:返回首页
    return {"message": "Hello World"}


if __name__ == '__main__':
    uvicorn.run(app='main:app', host="127.0.0.1", port=8000, reload=True, debug=True)
