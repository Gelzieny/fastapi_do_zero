from http import HTTPStatus
from fastapi import APIRouter, HTTPException

from App.model.schemas import UserPublic, UserSchema


usuarios = APIRouter(tags=["Usuarios"])

@usuarios.post('/users', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
  return user