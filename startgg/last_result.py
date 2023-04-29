from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import ActivityState


class LastResult(BaseModel):
    user: Optional["LastResultUser"]


class LastResultUser(BaseModel):
    events: Optional["LastResultUserEvents"]


class LastResultUserEvents(BaseModel):
    nodes: Optional[List[Optional["LastResultUserEventsNodes"]]]


class LastResultUserEventsNodes(BaseModel):
    tournament: Optional["LastResultUserEventsNodesTournament"]
    id: Optional[str]
    name: Optional[str]
    num_entrants: Optional[int] = Field(alias="numEntrants")
    state: Optional[ActivityState]
    standings: Optional["LastResultUserEventsNodesStandings"]


class LastResultUserEventsNodesTournament(BaseModel):
    name: Optional[str]
    id: Optional[str]
    short_slug: Optional[str] = Field(alias="shortSlug")


class LastResultUserEventsNodesStandings(BaseModel):
    nodes: Optional[List[Optional["LastResultUserEventsNodesStandingsNodes"]]]


class LastResultUserEventsNodesStandingsNodes(BaseModel):
    entrant: Optional["LastResultUserEventsNodesStandingsNodesEntrant"]
    placement: Optional[int]
    is_final: Optional[bool] = Field(alias="isFinal")


class LastResultUserEventsNodesStandingsNodesEntrant(BaseModel):
    id: Optional[str]


LastResult.update_forward_refs()
LastResultUser.update_forward_refs()
LastResultUserEvents.update_forward_refs()
LastResultUserEventsNodes.update_forward_refs()
LastResultUserEventsNodesTournament.update_forward_refs()
LastResultUserEventsNodesStandings.update_forward_refs()
LastResultUserEventsNodesStandingsNodes.update_forward_refs()
LastResultUserEventsNodesStandingsNodesEntrant.update_forward_refs()
