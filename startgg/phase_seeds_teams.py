from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class PhaseSeedsTeams(BaseModel):
    phase: Optional["PhaseSeedsTeamsPhase"]


class PhaseSeedsTeamsPhase(BaseModel):
    id: Optional[str]
    seeds: Optional["PhaseSeedsTeamsPhaseSeeds"]


class PhaseSeedsTeamsPhaseSeeds(BaseModel):
    page_info: Optional["PhaseSeedsTeamsPhaseSeedsPageInfo"] = Field(alias="pageInfo")
    nodes: Optional[List[Optional["PhaseSeedsTeamsPhaseSeedsNodes"]]]


class PhaseSeedsTeamsPhaseSeedsPageInfo(BaseModel):
    total: Optional[int]
    total_pages: Optional[int] = Field(alias="totalPages")


class PhaseSeedsTeamsPhaseSeedsNodes(BaseModel):
    id: Optional[str]
    seed_num: Optional[int] = Field(alias="seedNum")
    entrant: Optional["PhaseSeedsTeamsPhaseSeedsNodesEntrant"]


class PhaseSeedsTeamsPhaseSeedsNodesEntrant(BaseModel):
    id: Optional[str]
    name: Optional[str]
    participants: Optional[
        List[Optional["PhaseSeedsTeamsPhaseSeedsNodesEntrantParticipants"]]
    ]


class PhaseSeedsTeamsPhaseSeedsNodesEntrantParticipants(BaseModel):
    id: Optional[str]
    gamer_tag: Optional[str] = Field(alias="gamerTag")


PhaseSeedsTeams.update_forward_refs()
PhaseSeedsTeamsPhase.update_forward_refs()
PhaseSeedsTeamsPhaseSeeds.update_forward_refs()
PhaseSeedsTeamsPhaseSeedsPageInfo.update_forward_refs()
PhaseSeedsTeamsPhaseSeedsNodes.update_forward_refs()
PhaseSeedsTeamsPhaseSeedsNodesEntrant.update_forward_refs()
PhaseSeedsTeamsPhaseSeedsNodesEntrantParticipants.update_forward_refs()
