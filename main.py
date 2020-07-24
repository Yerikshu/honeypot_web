from typing import List

import uvicorn
from fastapi import FastAPI

from apps.base_route import router
from test.base_route import GzipRoute

app = FastAPI()
app.include_router(router, prefix="/api")
# app.router.route_class = GzipRoute


# @app.post("/sum")
# async def sum_numbers(numbers: List[int] = Body(...)):
#     return {"sum": sum(numbers)}

@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == '__main__':
    uvicorn.run(app='main:app', host="127.0.0.1", port=8000, reload=True, debug=True)



