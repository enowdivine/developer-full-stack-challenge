from fastapi import FastAPI
from routes.user import user_router
from routes.author import author_router
from routes.book import book_router

app = FastAPI()

app.include_router(user_router)
app.include_router(author_router)
app.include_router(book_router)


@app.get("/", response_model=None)
def read_root():
    return {"Hello": "world"}
