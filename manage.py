from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from App.controller.user_controller import usuarios

app = FastAPI(
  title="FastAPI do Zero",
  version="0.1.0",
  description="API criada com FastAPI para fins didáticos"
)


app.include_router(usuarios)

@app.get("/apiname", include_in_schema=False, response_class=HTMLResponse)
async def apiname() -> str:
  return "FastAPI do Zero"


if __name__ == "__main__":
  import uvicorn
  uvicorn.run("manage:app", host="127.0.0.1", port=5092, log_level="info", reload=True)