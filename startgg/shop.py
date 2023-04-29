from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class Shop(BaseModel):
    shop: Optional["ShopShop"]


class ShopShop(BaseModel):
    id: Optional[str]
    name: Optional[str]
    slug: Optional[str]
    messages: Optional["ShopShopMessages"]
    levels: Optional["ShopShopLevels"]


class ShopShopMessages(BaseModel):
    nodes: Optional[List[Optional["ShopShopMessagesNodes"]]]


class ShopShopMessagesNodes(BaseModel):
    total: Optional[float]
    message: Optional[str]
    gamertag: Optional[str]
    name: Optional[str]


class ShopShopLevels(BaseModel):
    nodes: Optional[List[Optional["ShopShopLevelsNodes"]]]


class ShopShopLevelsNodes(BaseModel):
    name: Optional[str]
    goal_amount: Optional[float] = Field(alias="goalAmount")
    curr_amount: Optional[float] = Field(alias="currAmount")
    description: Optional[str]


Shop.update_forward_refs()
ShopShop.update_forward_refs()
ShopShopMessages.update_forward_refs()
ShopShopMessagesNodes.update_forward_refs()
ShopShopLevels.update_forward_refs()
ShopShopLevelsNodes.update_forward_refs()
