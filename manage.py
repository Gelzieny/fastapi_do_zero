from fastapi import FastAPI

app = FastAPI(
  title="FastAPI do Zero",
  version="0.1.0",
  description="API criada com FastAPI para fins didáticos"
)

@app.get("/")
async def root():
  return {"message": "Hello World"}


if __name__ == "__main__":
  import uvicorn
  uvicorn.run("manage:app", host="127.0.0.1", port=5092, log_level="info", reload=True)