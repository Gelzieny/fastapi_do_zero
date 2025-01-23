from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(
  title="FastAPI do Zero",
  version="0.1.0",
  description="API criada com FastAPI para fins didáticos"
)

@app.get('/', response_class=HTMLResponse)
async def root():
  return """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""


if __name__ == "__main__":
  import uvicorn
  uvicorn.run("manage:app", host="127.0.0.1", port=5092, log_level="info", reload=True)