from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class PhaseSeeds(BaseModel):
    phase: Optional["PhaseSeedsPhase"]


class PhaseSeedsPhase(BaseModel):
    id: Optional[str]
    seeds: Optional["PhaseSeedsPhaseSeeds"]


class PhaseSeedsPhaseSeeds(BaseModel):
    page_info: Optional["PhaseSeedsPhaseSeedsPageInfo"] = Field(alias="pageInfo")
    nodes: Optional[List[Optional["PhaseSeedsPhaseSeedsNodes"]]]


class PhaseSeedsPhaseSeedsPageInfo(BaseModel):
    total: Optional[int]
    total_pages: Optional[int] = Field(alias="totalPages")


class PhaseSeedsPhaseSeedsNodes(BaseModel):
    id: Optional[str]
    seed_num: Optional[int] = Field(alias="seedNum")
    entrant: Optional["PhaseSeedsPhaseSeedsNodesEntrant"]


class PhaseSeedsPhaseSeedsNodesEntrant(BaseModel):
    id: Optional[str]
    participants: Optional[
        List[Optional["PhaseSeedsPhaseSeedsNodesEntrantParticipants"]]
    ]


class PhaseSeedsPhaseSeedsNodesEntrantParticipants(BaseModel):
    id: Optional[str]
    gamer_tag: Optional[str] = Field(alias="gamerTag")


PhaseSeeds.update_forward_refs()
PhaseSeedsPhase.update_forward_refs()
PhaseSeedsPhaseSeeds.update_forward_refs()
PhaseSeedsPhaseSeedsPageInfo.update_forward_refs()
PhaseSeedsPhaseSeedsNodes.update_forward_refs()
PhaseSeedsPhaseSeedsNodesEntrant.update_forward_refs()
PhaseSeedsPhaseSeedsNodesEntrantParticipants.update_forward_refs()
