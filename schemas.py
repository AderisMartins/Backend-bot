from typing import Union
from pydantic import BaseModel, Field


class SocialCreateInput(BaseModel):
    social_media: str


class SocialListOutput(BaseModel):
    id: int
    social_media: str

    class Config:
        orm_mode = True


class SocialUpdateInput(BaseModel):
    social_media: str


class AccountCreateInput(BaseModel):
    email: str
    password: str
    social_id: int


class AccountListOutput(BaseModel):
    id: int
    email: str
    password: str
    social_id: int

    class Config:
        orm_mode = True


class AccountUpdateInput(BaseModel):
    email: str
    password: str
    social_id: int


class CreateOutput(BaseModel):
    message: str


class DeleteOutput(BaseModel):
    message: str


class ErrorOutput(BaseModel):
    error: str

#########################################################################################################
class SearchParamsInput(BaseModel):
    rede_social: str
    perfil: str

class SearchOutput(BaseModel):
    search_output: Union[str, None] = Field(
        default=None, title="The description of the error", max_length=300
    )

    class Config:
        orm_mode = True
