from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class Sets(BaseModel):
    player: Optional["SetsPlayer"]


class SetsPlayer(BaseModel):
    id: Optional[str]
    sets: Optional["SetsPlayerSets"]


class SetsPlayerSets(BaseModel):
    nodes: Optional[List[Optional["SetsPlayerSetsNodes"]]]


class SetsPlayerSetsNodes(BaseModel):
    id: Optional[str]
    display_score: Optional[str] = Field(alias="displayScore")
    event: Optional["SetsPlayerSetsNodesEvent"]


class SetsPlayerSetsNodesEvent(BaseModel):
    id: Optional[str]
    name: Optional[str]
    tournament: Optional["SetsPlayerSetsNodesEventTournament"]


class SetsPlayerSetsNodesEventTournament(BaseModel):
    id: Optional[str]
    name: Optional[str]


Sets.update_forward_refs()
SetsPlayer.update_forward_refs()
SetsPlayerSets.update_forward_refs()
SetsPlayerSetsNodes.update_forward_refs()
SetsPlayerSetsNodesEvent.update_forward_refs()
SetsPlayerSetsNodesEventTournament.update_forward_refs()
