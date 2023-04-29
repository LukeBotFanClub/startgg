from typing import List, Optional

from .base_model import BaseModel


class SetsAtStation(BaseModel):
    event: Optional["SetsAtStationEvent"]


class SetsAtStationEvent(BaseModel):
    id: Optional[str]
    name: Optional[str]
    sets: Optional["SetsAtStationEventSets"]


class SetsAtStationEventSets(BaseModel):
    nodes: Optional[List[Optional["SetsAtStationEventSetsNodes"]]]


class SetsAtStationEventSetsNodes(BaseModel):
    id: Optional[str]
    station: Optional["SetsAtStationEventSetsNodesStation"]
    slots: Optional[List[Optional["SetsAtStationEventSetsNodesSlots"]]]


class SetsAtStationEventSetsNodesStation(BaseModel):
    id: Optional[str]
    number: Optional[int]


class SetsAtStationEventSetsNodesSlots(BaseModel):
    id: Optional[str]
    entrant: Optional["SetsAtStationEventSetsNodesSlotsEntrant"]


class SetsAtStationEventSetsNodesSlotsEntrant(BaseModel):
    id: Optional[str]
    name: Optional[str]


SetsAtStation.update_forward_refs()
SetsAtStationEvent.update_forward_refs()
SetsAtStationEventSets.update_forward_refs()
SetsAtStationEventSetsNodes.update_forward_refs()
SetsAtStationEventSetsNodesStation.update_forward_refs()
SetsAtStationEventSetsNodesSlots.update_forward_refs()
SetsAtStationEventSetsNodesSlotsEntrant.update_forward_refs()
