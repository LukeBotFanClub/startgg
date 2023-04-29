from datetime import datetime
from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class Upcoming(BaseModel):
    user: Optional["UpcomingUser"]


class UpcomingUser(BaseModel):
    tournaments: Optional["UpcomingUserTournaments"]


class UpcomingUserTournaments(BaseModel):
    nodes: Optional[List[Optional["UpcomingUserTournamentsNodes"]]]


class UpcomingUserTournamentsNodes(BaseModel):
    name: Optional[str]
    id: Optional[str]
    short_slug: Optional[str] = Field(alias="shortSlug")
    start_at: Optional[datetime] = Field(alias="startAt")
    state: Optional[int]
    events: Optional[List[Optional["UpcomingUserTournamentsNodesEvents"]]]


class UpcomingUserTournamentsNodesEvents(BaseModel):
    id: Optional[str]
    name: Optional[str]
    videogame: Optional["UpcomingUserTournamentsNodesEventsVideogame"]
    entrants: Optional["UpcomingUserTournamentsNodesEventsEntrants"]


class UpcomingUserTournamentsNodesEventsVideogame(BaseModel):
    id: Optional[str]


class UpcomingUserTournamentsNodesEventsEntrants(BaseModel):
    nodes: Optional[List[Optional["UpcomingUserTournamentsNodesEventsEntrantsNodes"]]]


class UpcomingUserTournamentsNodesEventsEntrantsNodes(BaseModel):
    id: Optional[str]


Upcoming.update_forward_refs()
UpcomingUser.update_forward_refs()
UpcomingUserTournaments.update_forward_refs()
UpcomingUserTournamentsNodes.update_forward_refs()
UpcomingUserTournamentsNodesEvents.update_forward_refs()
UpcomingUserTournamentsNodesEventsVideogame.update_forward_refs()
UpcomingUserTournamentsNodesEventsEntrants.update_forward_refs()
UpcomingUserTournamentsNodesEventsEntrantsNodes.update_forward_refs()
