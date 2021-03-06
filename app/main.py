# https://fastapi.tiangolo.com/tutorial/first-steps/
# How to run the code: uvicorn app.main:app --reload

from fastapi import FastAPI

from app.routers import file

# Import your routers here
# example: from app.routers import module1

app = FastAPI(
    title="File Uploader API",
    description="API example to upload file to server :))",
    version="0.1.0",
    contact={
        "name": "Your Name",
        "url": "http://you-own-url.com"
    }
)

app.include_router(file.router)

# use the imported router in your project here:
# app.include_router(module1.router)


@app.get("/")
async def root_endpoint():
    return {
        "message": "API is running successfully!"
    }
