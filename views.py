from typing import List
from fastapi import APIRouter, HTTPException

from services import socialService, accountService, searchService
from schemas import AccountCreateInput, SocialCreateInput, CreateOutput, ErrorOutput, DeleteOutput, SocialListOutput, \
    AccountListOutput, SocialUpdateInput, AccountUpdateInput, SearchOutput, SearchParamsInput

social_router = APIRouter(prefix='/social')
account_router = APIRouter(prefix='/account')
search_router = APIRouter(prefix='/search')

########################  Social Route ####################################################

@social_router.post('/create', response_model=CreateOutput, responses={400: {'model': ErrorOutput}})
async def social_create(user_input: SocialCreateInput):
    try:
        await socialService.create_social(user_input.social_media)
        return CreateOutput(message='Ok')
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@social_router.delete('/delete/{id}', response_model=DeleteOutput, responses={400: {'model': ErrorOutput}})
async def social_delete(id: int):
    try:
        await socialService.delete_social(id)
        return DeleteOutput(message='Ok')
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@social_router.get('/', response_model=List[SocialListOutput], responses={400: {'model': ErrorOutput}})
async def social_list():
    try:
        return await socialService.list_social()
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@social_router.get('/{id}', response_model=SocialListOutput, responses={400: {'model': ErrorOutput}})
async def show_social(id: int):
    try:
        return await socialService.show_social(id)
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@social_router.put('/update/{id}', response_model=SocialListOutput, responses={400: {'model': ErrorOutput}})
async def update_social(id: int, social: SocialUpdateInput):
    try:
        return await socialService.update_social(id, social)
    except Exception as error:
        raise HTTPException(400, detail=str(error))


#######################  Account Route  ####################################################

@account_router.post('/create', response_model=CreateOutput, responses={400: {'model': ErrorOutput}})
async def account_create(user_input: AccountCreateInput):
    try:
        await accountService.create_account(user_input.email, user_input.password, user_input.social_id)
        return CreateOutput(message='Ok')
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@account_router.delete('/delete/{id}', response_model=DeleteOutput, responses={400: {'model': ErrorOutput}})
async def account_delete(id: int):
    try:
        await accountService.delete_account(id)
        return DeleteOutput(message='Ok')
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@account_router.get('/', response_model=List[AccountListOutput], responses={400: {'model': ErrorOutput}})
async def account_list():
    try:
        return await accountService.list_account()
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@account_router.get('/{id}', response_model=AccountListOutput, responses={400: {'model': ErrorOutput}})
async def show_account(id: int):
    try:
        return await accountService.show_account(id)
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@account_router.put('/update/{id}', response_model=AccountListOutput, responses={400: {'model': ErrorOutput}})
async def update_account(id: int, account: AccountUpdateInput):
    try:
        return await accountService.update_account(id, account)
    except Exception as error:
        raise HTTPException(400, detail=str(error))


#######################  Search Route  ####################################################

@search_router.post('/', response_model=SearchOutput, response_model_exclude_unset=True)
async def search(params: SearchParamsInput):
   try:
      return searchService.search(params.rede_social, params.perfil)
   except Exception as error:
      raise HTTPException(400, detail=str(error))
