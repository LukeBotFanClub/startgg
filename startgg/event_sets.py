from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class EventSets(BaseModel):
    event: Optional["EventSetsEvent"]


class EventSetsEvent(BaseModel):
    id: Optional[str]
    name: Optional[str]
    sets: Optional["EventSetsEventSets"]


class EventSetsEventSets(BaseModel):
    page_info: Optional["EventSetsEventSetsPageInfo"] = Field(alias="pageInfo")
    nodes: Optional[List[Optional["EventSetsEventSetsNodes"]]]


class EventSetsEventSetsPageInfo(BaseModel):
    total: Optional[int]


class EventSetsEventSetsNodes(BaseModel):
    id: Optional[str]
    slots: Optional[List[Optional["EventSetsEventSetsNodesSlots"]]]


class EventSetsEventSetsNodesSlots(BaseModel):
    id: Optional[str]
    entrant: Optional["EventSetsEventSetsNodesSlotsEntrant"]


class EventSetsEventSetsNodesSlotsEntrant(BaseModel):
    id: Optional[str]
    name: Optional[str]


EventSets.update_forward_refs()
EventSetsEvent.update_forward_refs()
EventSetsEventSets.update_forward_refs()
EventSetsEventSetsPageInfo.update_forward_refs()
EventSetsEventSetsNodes.update_forward_refs()
EventSetsEventSetsNodesSlots.update_forward_refs()
EventSetsEventSetsNodesSlotsEntrant.update_forward_refs()
