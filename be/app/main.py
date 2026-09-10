from fastapi import FastAPI


app = FastAPI(
    title="CariKampus API",
    description="Backend API CariKampus",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "CariKampus API Running"
    }