from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class GamerTag(BaseModel):
    user: Optional["GamerTagUser"]


class GamerTagUser(BaseModel):
    id: Optional[str]
    slug: Optional[str]
    player: Optional["GamerTagUserPlayer"]


class GamerTagUserPlayer(BaseModel):
    gamer_tag: Optional[str] = Field(alias="gamerTag")


GamerTag.update_forward_refs()
GamerTagUser.update_forward_refs()
GamerTagUserPlayer.update_forward_refs()
