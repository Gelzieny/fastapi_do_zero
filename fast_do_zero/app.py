from fastapi import FastAPI

app = FastAPI(
    title='FastApi do Zero',
    description='Curso de FastAPI do Zero',
)


@app.get('/')
def read_root():
    return {'message': 'Hello World'}
