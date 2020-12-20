from typing import List, Optional, Callable

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

models = []

NOT_FOUND = HTTPException(404, 'Item not found')


class CRUDGenerator(APIRouter):
    model_cls: BaseModel = None
    _base_path: str = '/'

    def __init__(self, model: BaseModel, *args, **kwargs):
        self.model_cls = model
        self._base_path += self.model_cls.__name__.lower()

        super().__init__(prefix=self._base_path, tags=[self._base_path.strip('/')], *args, **kwargs)

        super().add_api_route('', self.get_all(), methods=['GET'], response_model=Optional[List[self.model_cls]])
        super().add_api_route('', self.create(), methods=['POST'], response_model=self.model_cls)
        super().add_api_route('', self.delete_all(), methods=['DELETE'], response_model=Optional[List[self.model_cls]])

        super().add_api_route('/{item_id}', self.get_one(), methods=['GET'], response_model=self.model_cls)
        super().add_api_route('/{item_id}', self.update(), methods=['POST'], response_model=self.model_cls)
        super().add_api_route('/{item_id}', self.delete_one(), methods=['DELETE'], response_model=self.model_cls)

    def get_all(self, *args, **kwargs) -> Callable:
        raise NotImplementedError

    def get_one(self, *args, **kwargs) -> Callable:
        raise NotImplementedError

    def create(self, *args, **kwargs) -> Callable:
        raise NotImplementedError

    def update(self, *args, **kwargs) -> Callable:
        raise NotImplementedError

    def delete_one(self, *args, **kwargs) -> Callable:
        raise NotImplementedError

    def delete_all(self, *args, **kwargs) -> Callable:
        raise NotImplementedError
