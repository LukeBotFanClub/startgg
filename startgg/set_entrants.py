from typing import List, Optional

from pydantic import Field, Json

from .base_model import BaseModel


class SetEntrants(BaseModel):
    set: Optional["SetEntrantsSet"]


class SetEntrantsSet(BaseModel):
    id: Optional[str]
    slots: Optional[List[Optional["SetEntrantsSetSlots"]]]


class SetEntrantsSetSlots(BaseModel):
    id: Optional[str]
    entrant: Optional["SetEntrantsSetSlotsEntrant"]


class SetEntrantsSetSlotsEntrant(BaseModel):
    id: Optional[str]
    name: Optional[str]
    participants: Optional[List[Optional["SetEntrantsSetSlotsEntrantParticipants"]]]


class SetEntrantsSetSlotsEntrantParticipants(BaseModel):
    id: Optional[str]
    gamer_tag: Optional[str] = Field(alias="gamerTag")
    connected_accounts: Optional[Json] = Field(alias="connectedAccounts")


SetEntrants.update_forward_refs()
SetEntrantsSet.update_forward_refs()
SetEntrantsSetSlots.update_forward_refs()
SetEntrantsSetSlotsEntrant.update_forward_refs()
SetEntrantsSetSlotsEntrantParticipants.update_forward_refs()
