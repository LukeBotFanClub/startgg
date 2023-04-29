from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class LeagueStandings(BaseModel):
    league: Optional["LeagueStandingsLeague"]


class LeagueStandingsLeague(BaseModel):
    id: Optional[str]
    name: Optional[str]
    standings: Optional["LeagueStandingsLeagueStandings"]


class LeagueStandingsLeagueStandings(BaseModel):
    page_info: Optional["LeagueStandingsLeagueStandingsPageInfo"] = Field(
        alias="pageInfo"
    )
    nodes: Optional[List[Optional["LeagueStandingsLeagueStandingsNodes"]]]


class LeagueStandingsLeagueStandingsPageInfo(BaseModel):
    total_pages: Optional[int] = Field(alias="totalPages")
    total: Optional[int]


class LeagueStandingsLeagueStandingsNodes(BaseModel):
    id: Optional[str]
    placement: Optional[int]
    entrant: Optional["LeagueStandingsLeagueStandingsNodesEntrant"]


class LeagueStandingsLeagueStandingsNodesEntrant(BaseModel):
    id: Optional[str]
    name: Optional[str]


LeagueStandings.update_forward_refs()
LeagueStandingsLeague.update_forward_refs()
LeagueStandingsLeagueStandings.update_forward_refs()
LeagueStandingsLeagueStandingsPageInfo.update_forward_refs()
LeagueStandingsLeagueStandingsNodes.update_forward_refs()
LeagueStandingsLeagueStandingsNodesEntrant.update_forward_refs()
