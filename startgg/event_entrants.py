from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class EventEntrants(BaseModel):
    event: Optional["EventEntrantsEvent"]


class EventEntrantsEvent(BaseModel):
    id: Optional[str]
    name: Optional[str]
    entrants: Optional["EventEntrantsEventEntrants"]


class EventEntrantsEventEntrants(BaseModel):
    page_info: Optional["EventEntrantsEventEntrantsPageInfo"] = Field(alias="pageInfo")
    nodes: Optional[List[Optional["EventEntrantsEventEntrantsNodes"]]]


class EventEntrantsEventEntrantsPageInfo(BaseModel):
    total: Optional[int]
    total_pages: Optional[int] = Field(alias="totalPages")


class EventEntrantsEventEntrantsNodes(BaseModel):
    id: Optional[str]
    participants: Optional[
        List[Optional["EventEntrantsEventEntrantsNodesParticipants"]]
    ]


class EventEntrantsEventEntrantsNodesParticipants(BaseModel):
    id: Optional[str]
    gamer_tag: Optional[str] = Field(alias="gamerTag")


EventEntrants.update_forward_refs()
EventEntrantsEvent.update_forward_refs()
EventEntrantsEventEntrants.update_forward_refs()
EventEntrantsEventEntrantsPageInfo.update_forward_refs()
EventEntrantsEventEntrantsNodes.update_forward_refs()
EventEntrantsEventEntrantsNodesParticipants.update_forward_refs()
