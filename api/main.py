from fastapi import FastAPI

app = FastAPI()


# Test Route.
@app.get("/")
def root():
    return {"message": "Hello, Friend!"}
