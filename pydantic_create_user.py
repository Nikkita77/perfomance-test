"""
Pydantic-модели для эндпоинта POST /api/v1/users (создание пользователя).
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, EmailStr, Field, constr


class UserSchema(BaseModel):
    """
    Модель данных пользователя.

    Пример:
    {
      "id": "string",
      "email": "user@example.com",
      "lastName": "string",
      "firstName": "string",
      "middleName": "string",
      "phoneNumber": "string"
    }
    """

    model_config = ConfigDict(extra="forbid")

    id: constr(strip_whitespace=True, min_length=1) = Field(
        ...,
        description="Идентификатор пользователя.",
        examples=["8ac86aee-405e-455e-992b-6cd59449ca9d"],
    )
    email: EmailStr = Field(
        ...,
        description="Email пользователя.",
        examples=["user@example.com"],
    )
    lastName: constr(strip_whitespace=True, min_length=1) = Field(
        ...,
        description="Фамилия пользователя.",
        examples=["Ivanov"],
    )
    firstName: constr(strip_whitespace=True, min_length=1) = Field(
        ...,
        description="Имя пользователя.",
        examples=["Ivan"],
    )
    middleName: constr(strip_whitespace=True, min_length=1) = Field(
        ...,
        description="Отчество пользователя.",
        examples=["Ivanovich"],
    )
    phoneNumber: constr(strip_whitespace=True, min_length=3, max_length=32) = Field(
        ...,
        description="Номер телефона пользователя (формат зависит от API).",
        examples=["79990000000"],
    )


class CreateUserRequestSchema(BaseModel):
    """
    Запрос на создание пользователя (POST /api/v1/users).

    Пример:
    {
      "email": "user@example.com",
      "lastName": "string",
      "firstName": "string",
      "middleName": "string",
      "phoneNumber": "string"
    }
    """

    model_config = ConfigDict(extra="forbid")

    email: EmailStr = Field(
        ...,
        description="Email пользователя.",
        examples=["user@example.com"],
    )
    lastName: constr(strip_whitespace=True, min_length=1) = Field(
        ...,
        description="Фамилия пользователя.",
        examples=["Ivanov"],
    )
    firstName: constr(strip_whitespace=True, min_length=1) = Field(
        ...,
        description="Имя пользователя.",
        examples=["Ivan"],
    )
    middleName: constr(strip_whitespace=True, min_length=1) = Field(
        ...,
        description="Отчество пользователя.",
        examples=["Ivanovich"],
    )
    phoneNumber: constr(strip_whitespace=True, min_length=3, max_length=32) = Field(
        ...,
        description="Номер телефона пользователя (формат зависит от API).",
        examples=["79990000000"],
    )


class CreateUserResponseSchema(BaseModel):
    """
    Ответ на создание пользователя (POST /api/v1/users).

    Пример:
    {
      "user": {
        "id": "string",
        "email": "user@example.com",
        "lastName": "string",
        "firstName": "string",
        "middleName": "string",
        "phoneNumber": "string"
      }
    }
    """

    model_config = ConfigDict(extra="forbid")

    user: UserSchema = Field(
        ...,
        description="Созданный пользователь.",
    )