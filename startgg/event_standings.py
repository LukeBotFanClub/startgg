from typing import List, Optional

from .base_model import BaseModel


class EventStandings(BaseModel):
    event: Optional["EventStandingsEvent"]


class EventStandingsEvent(BaseModel):
    id: Optional[str]
    name: Optional[str]
    standings: Optional["EventStandingsEventStandings"]


class EventStandingsEventStandings(BaseModel):
    nodes: Optional[List[Optional["EventStandingsEventStandingsNodes"]]]


class EventStandingsEventStandingsNodes(BaseModel):
    placement: Optional[int]
    entrant: Optional["EventStandingsEventStandingsNodesEntrant"]


class EventStandingsEventStandingsNodesEntrant(BaseModel):
    id: Optional[str]
    name: Optional[str]


EventStandings.update_forward_refs()
EventStandingsEvent.update_forward_refs()
EventStandingsEventStandings.update_forward_refs()
EventStandingsEventStandingsNodes.update_forward_refs()
EventStandingsEventStandingsNodesEntrant.update_forward_refs()
