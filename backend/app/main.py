from fastapi import FastAPI
from merge import router as merge_router


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Merge Sort App"}

app.include_router(merge_router)

