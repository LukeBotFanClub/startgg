from datetime import datetime
from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class LeagueSchedule(BaseModel):
    league: Optional["LeagueScheduleLeague"]


class LeagueScheduleLeague(BaseModel):
    id: Optional[str]
    name: Optional[str]
    events: Optional["LeagueScheduleLeagueEvents"]


class LeagueScheduleLeagueEvents(BaseModel):
    page_info: Optional["LeagueScheduleLeagueEventsPageInfo"] = Field(alias="pageInfo")
    nodes: Optional[List[Optional["LeagueScheduleLeagueEventsNodes"]]]


class LeagueScheduleLeagueEventsPageInfo(BaseModel):
    total_pages: Optional[int] = Field(alias="totalPages")
    total: Optional[int]


class LeagueScheduleLeagueEventsNodes(BaseModel):
    id: Optional[str]
    name: Optional[str]
    start_at: Optional[datetime] = Field(alias="startAt")
    tournament: Optional["LeagueScheduleLeagueEventsNodesTournament"]


class LeagueScheduleLeagueEventsNodesTournament(BaseModel):
    id: Optional[str]
    name: Optional[str]


LeagueSchedule.update_forward_refs()
LeagueScheduleLeague.update_forward_refs()
LeagueScheduleLeagueEvents.update_forward_refs()
LeagueScheduleLeagueEventsPageInfo.update_forward_refs()
LeagueScheduleLeagueEventsNodes.update_forward_refs()
LeagueScheduleLeagueEventsNodesTournament.update_forward_refs()
